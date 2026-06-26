from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "paper_writing_obsidian_vault"
ITER_DIR = VAULT / "70_Iterative_Thinking"
TOTAL_MEMORY_SRC = Path(os.environ.get("TOTAL_MEMORY_SRC", ROOT / "total-agent-memory" / "src"))

PAPER_LAYERS = [
    "45_Supervision",
    "40_Final_Generalized_Rules",
    "50_Conflicts",
    "60_Limited_Rules",
    "30_Writing_Rules",
]
WORKFLOW_LAYERS = ["35_Workflow_Governance"]
EVIDENCE_LAYERS = ["20_Paper_Memories"]
DEFAULT_CODEX_CONDITIONS = ITER_DIR / "kb_rag_codex_conditions.json"
EVIDENCE_SCORE_WEIGHTS = {
    "hit_conflict": 3,
    "hit_limited": 2,
    "no_final_rule": 2,
    "user_requests_evidence": 3,
    "high_risk_topic": 2,
    "formal_manuscript_edit": 1,
    "score_margin_lt_20_pct": 1,
    "mentor_or_old_error_risk": 2,
    "low_evidence_support": 1,
}

FAILURE_TERMS = {
    "failure",
    "fail",
    "error",
    "bug",
    "pitfall",
    "fix",
    "repair",
    "regression",
    "失败",
    "报错",
    "错误",
    "踩坑",
    "修复",
    "回归",
}
WORKFLOW_TERMS = {
    "workflow",
    "governance",
    "automation",
    "memory",
    "knowledge base",
    "process",
    "工作流",
    "流程",
    "自动化",
    "记忆",
    "知识库",
}
QUERY_EXPANSIONS = {
    "摘要": ["abstract"],
    "开头": ["opening", "first sentence"],
    "首句": ["first sentence", "opening"],
    "界面波": ["interface wave"],
    "金属间化合物": ["intermetallic compound", "Al3Ti"],
    "厚度": ["thickness"],
    "分布": ["distribution"],
    "引言": ["introduction"],
    "文献综述": ["literature review", "literature"],
    "文献": ["literature", "reference", "citation"],
    "实验": ["experiment", "experimental"],
    "模拟": ["simulation", "SPH", "SPH-FEM"],
    "差距": ["gap", "missing", "limitation"],
    "参考文献": ["reference", "citation"],
    "替换": ["replacement", "upgrade"],
    "导师": ["mentor"],
    "工作流": ["workflow", "process governance", "workflow governance"],
    "流程": ["process", "governance"],
    "论文要求": ["manuscript requirements", "paper requirements"],
    "混淆": ["separate", "must not", "conflict"],
    "知识库": ["knowledge base", "knowledge-base maintenance"],
}


@dataclass
class Note:
    kid: int
    path: Path
    rel: str
    layer: str
    title: str
    tags: list[str]
    text: str
    summary: str
    ktype: str
    links: list[str]
    incoming: list[str]


def read_text(path: Path) -> str:
    for enc in ("utf-8-sig", "utf-8", "gb18030"):
        try:
            return path.read_text(encoding=enc, errors="strict")
        except UnicodeError:
            continue
    return path.read_text(encoding="utf-8", errors="replace")


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def parse_frontmatter(text: str) -> tuple[dict[str, str], list[str], str]:
    match = re.match(r"^---\s*\n([\s\S]*?)\n---\s*\n?", text)
    if not match:
        return {}, [], text
    meta: dict[str, str] = {}
    tags: list[str] = []
    current_key = ""
    for line in match.group(1).splitlines():
        if re.match(r"^\w", line):
            key, _, value = line.partition(":")
            current_key = key.strip()
            if current_key == "tags":
                if value.strip():
                    tags.extend(t.strip() for t in value.split(",") if t.strip())
            else:
                meta[current_key] = value.strip()
            continue
        if current_key == "tags":
            item = re.match(r"^\s*-\s*(.+?)\s*$", line)
            if item:
                tags.append(item.group(1).strip())
    return meta, sorted(set(tags)), text[match.end() :]


def section(text: str, heading: str) -> str:
    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*$([\s\S]*?)(?=^##\s+|\Z)",
        re.MULTILINE,
    )
    match = pattern.search(text)
    return match.group(1).strip() if match else ""


def compact_summary(body: str, title: str) -> str:
    for heading in (
        "Final Generalized Rule",
        "Current Rule",
        "Generalized Rule",
        "Governance Rule",
        "Reusable Rule",
        "Why this needs user analysis",
        "Problem Pattern",
    ):
        found = section(body, heading)
        if found:
            return re.sub(r"\s+", " ", found).strip()[:480]
    clean = re.sub(r"^# .*$", "", body, flags=re.MULTILINE)
    clean = re.sub(r"\s+", " ", clean).strip()
    return (clean or title)[:480]


def parse_wikilinks(text: str) -> list[str]:
    links: list[str] = []
    for raw in re.findall(r"\[\[([^\]]+)\]\]", text):
        target = raw.split("|", 1)[0].split("#", 1)[0].strip()
        if target:
            links.append(Path(target).stem)
    return sorted(set(links))


def layer_for(rel: Path) -> str:
    return rel.parent.as_posix()


def note_type(layer: str, tags: list[str]) -> str:
    lowered = {tag.lower() for tag in tags}
    if layer == "35_Workflow_Governance" or "workflow-governance" in lowered:
        return "lesson"
    if layer == "45_Supervision":
        return "solution"
    if layer == "50_Conflicts":
        return "fact"
    if layer == "60_Limited_Rules":
        return "lesson"
    if layer == "40_Final_Generalized_Rules":
        return "decision"
    return "lesson"


def load_notes(layers: list[str]) -> list[Note]:
    notes: list[Note] = []
    kid = 1
    for layer in layers:
        folder = VAULT / layer
        if not folder.exists():
            continue
        for path in sorted(folder.glob("*.md")):
            if path.name == "README.md" or path.name.startswith("TEMPLATE"):
                continue
            raw = read_text(path)
            meta, tags, body = parse_frontmatter(raw)
            lowered_tags = {tag.lower() for tag in tags}
            note_status = (meta.get("status") or section(body, "status")).strip().lower()
            if "superseded" in lowered_tags or note_status == "superseded":
                continue
            rel = path.relative_to(VAULT)
            title = meta.get("title") or path.stem
            notes.append(
                Note(
                    kid=kid,
                    path=path,
                    rel=rel.as_posix(),
                    layer=layer_for(rel),
                    title=title,
                    tags=tags,
                    text=raw,
                    summary=compact_summary(body, title),
                    ktype=note_type(layer, tags),
                    links=parse_wikilinks(raw),
                    incoming=[],
                )
            )
            kid += 1
    return notes


def attach_incoming_links(notes: list[Note]) -> None:
    by_stem = {Path(note.rel).stem: note for note in notes}
    for note in notes:
        note.incoming = []
    for note in notes:
        for link in note.links:
            target = by_stem.get(link)
            if target and note.title not in target.incoming:
                target.incoming.append(note.title)
    for note in notes:
        note.incoming.sort()


def terms(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9_\-/]+|[\u4e00-\u9fff]{1,4}", text.lower())


def expanded_query_terms(query: str) -> list[str]:
    out = terms(query)
    lowered = query.lower()
    for key, values in QUERY_EXPANSIONS.items():
        if key.lower() in lowered:
            out.extend(value.lower() for value in values)
    deduped: list[str] = []
    for term in out:
        if term and term not in deduped:
            deduped.append(term)
    return deduped


def lexical_score(query: str, note: Note, phase: str | None) -> float:
    q_terms = expanded_query_terms(query)
    hay = "\n".join([note.title, note.rel, " ".join(note.tags), note.summary, note.text[:1200]]).lower()
    if not q_terms:
        return 0.0
    score = 0.0
    for term in q_terms:
        if term in hay:
            score += 1.0
            if term in note.title.lower():
                score += 0.8
            if term in note.summary.lower():
                score += 0.5
    if any(term in query.lower() for term in FAILURE_TERMS):
        if note.ktype in {"solution", "lesson"}:
            score *= 1.35
        if any(tag.lower() in {"errors", "error", "pitfalls", "bugfix", "no-regression"} for tag in note.tags):
            score *= 1.15
    if phase and f"phase:{phase}".lower() in {tag.lower() for tag in note.tags}:
        score *= 1.15
    layer_boost = {
        "45_Supervision": 1.45,
        "40_Final_Generalized_Rules": 1.30,
        "50_Conflicts": 1.15,
        "60_Limited_Rules": 1.10,
        "30_Writing_Rules": 1.00,
        "35_Workflow_Governance": 1.20,
    }.get(note.layer, 0.90)
    return score * layer_boost


class _SummaryDB:
    def __init__(self, notes: list[Note]) -> None:
        self.notes = {note.kid: note for note in notes}
        self.ids: list[int] = []

    def execute(self, _sql: str, ids: list[int]) -> "_SummaryDB":
        self.ids = [int(i) for i in ids]
        return self

    def fetchall(self) -> list[dict[str, Any]]:
        return [
            {
                "knowledge_id": kid,
                "representation": "summary",
                "content": self.notes[kid].summary,
            }
            for kid in self.ids
            if kid in self.notes and self.notes[kid].summary
        ]


class _SummaryStore:
    def __init__(self, notes: list[Note]) -> None:
        self.db = _SummaryDB(notes)


def rag_response(search_result: dict[str, Any], store: Any, *, query: str, phase: str | None, limit: int) -> dict[str, Any]:
    if str(TOTAL_MEMORY_SRC) not in sys.path:
        sys.path.insert(0, str(TOTAL_MEMORY_SRC))
    try:
        from recall_modes import rag_response as total_memory_rag_response
    except ModuleNotFoundError:
        return local_rag_response(search_result, store, query=query, phase=phase, limit=limit)

    return total_memory_rag_response(search_result, store, query=query, phase=phase, limit=limit)


def local_rag_response(search_result: dict[str, Any], store: Any, *, query: str, phase: str | None, limit: int) -> dict[str, Any]:
    candidates: list[dict[str, Any]] = []
    for group in search_result.get("results", {}).values():
        candidates.extend(group)
    candidates.sort(key=lambda item: (-float(item.get("score", 0.0) or 0.0), str(item.get("path", ""))))
    selected = candidates[: max(1, limit)]
    ids = [int(item["id"]) for item in selected if "id" in item]
    summaries = {row["knowledge_id"]: row["content"] for row in store.db.execute("", ids).fetchall()}
    results: list[dict[str, Any]] = []
    total_tokens = 0
    for item in selected:
        kid = int(item["id"])
        summary = summaries.get(kid) or item.get("content", "")
        tokens = estimate_tokens(str(summary))
        total_tokens += tokens
        results.append(
            {
                "id": kid,
                "title": item.get("title", ""),
                "summary": summary,
                "summary_source": "local-summary",
                "type": item.get("type", "note"),
                "project": item.get("project", "paper_writing_obsidian_vault"),
                "score": item.get("score", 0),
                "importance": item.get("importance", "medium"),
                "created_at": item.get("created_at", ""),
                "related_ids": [],
                "duplicate_count": 1,
                "phase_match": bool(phase and f"phase:{phase}" in [str(tag).lower() for tag in item.get("tags", [])]),
                "preference_match": False,
                "_tokens": tokens,
            }
        )
    return {
        "query": query,
        "mode": "local-rag",
        "total": len(results),
        "candidate_total": len(candidates),
        "total_tokens": total_tokens,
        "strategy": {
            "retrieval": "local_lexical_graph_fallback",
            "dedupe": "none",
            "summary_cache": "markdown_frontmatter_summary_or_excerpt",
            "failure_priority": False,
            "preference_priority": False,
            "phase": phase or "",
            "next_step": "Open selected_files from this report when full evidence is needed.",
        },
        "results": results,
    }


def build_search_result(query: str, notes: list[Note], phase: str | None, candidate_limit: int) -> dict[str, Any]:
    attach_incoming_links(notes)
    raw_scores: dict[int, float] = {}
    for note in notes:
        score = lexical_score(query, note, phase)
        if score > 0:
            raw_scores[note.kid] = score
    by_stem = {Path(note.rel).stem: note for note in notes}
    by_title = {note.title: note for note in notes}
    graph_scores = dict(raw_scores)
    for note in notes:
        base = raw_scores.get(note.kid, 0.0)
        if base <= 0:
            continue
        for link in note.links:
            target = by_stem.get(link) or by_title.get(link)
            if target:
                graph_scores[target.kid] = max(graph_scores.get(target.kid, 0.0), base * 0.35)
        for incoming_title in note.incoming:
            source = by_title.get(incoming_title)
            if source:
                graph_scores[source.kid] = max(graph_scores.get(source.kid, 0.0), base * 0.25)
    scored: list[tuple[float, Note]] = [(score, note) for note in notes if (score := graph_scores.get(note.kid, 0.0)) > 0]
    if not scored:
        scored = [(0.01, note) for note in notes]
    scored.sort(key=lambda item: (-item[0], item[1].rel))
    grouped: dict[str, list[dict[str, Any]]] = {}
    for score, note in scored[:candidate_limit]:
        grouped.setdefault(note.ktype, []).append(
            {
                "id": note.kid,
                "title": note.title,
                "content": f"{note.title}\n{note.summary}",
                "type": note.ktype,
                "project": "paper_writing_obsidian_vault",
                "tags": note.tags,
                "score": round(score, 6),
                "created_at": "",
                "importance": "medium",
                "path": note.rel,
                "layer": note.layer,
                "graph": {
                    "outgoing_links": note.links,
                    "incoming_links": note.incoming,
                    "relation_score": len(note.links) + len(note.incoming),
                    "score_source": "lexical_or_graph_expanded",
                },
            }
        )
    return {"query": query, "results": grouped}


def wants_workflow(query: str, phase: str | None) -> bool:
    q = (query or "").lower()
    return bool(phase and phase.lower() in {"workflow", "governance"}) or any(term in q for term in WORKFLOW_TERMS)


def allowed_layers(query: str, phase: str | None, include_evidence: bool, include_workflow: bool | None) -> list[str]:
    workflow = wants_workflow(query, phase) if include_workflow is None else include_workflow
    layers = WORKFLOW_LAYERS[:] if workflow else PAPER_LAYERS[:]
    if include_evidence:
        layers += EVIDENCE_LAYERS
    return layers


def selected_note_ids(rag: dict[str, Any], limit: int, include_related: bool = False) -> list[int]:
    ids: list[int] = []
    for entry in rag.get("results", [])[:limit]:
        raw_ids = entry.get("related_ids") or [entry.get("id")]
        if not include_related:
            raw_ids = [entry.get("id")]
        for raw in raw_ids:
            try:
                kid = int(raw)
            except Exception:
                continue
            if kid not in ids:
                ids.append(kid)
    return ids


def load_codex_conditions(path: Path | None) -> dict[str, dict[str, bool]]:
    source = path or DEFAULT_CODEX_CONDITIONS
    if not source.exists():
        return {}
    try:
        raw = json.loads(source.read_text(encoding="utf-8-sig"))
    except Exception:
        return {}
    if isinstance(raw, dict) and "queries" in raw and isinstance(raw["queries"], dict):
        return {
            str(query): {str(k): bool(v) for k, v in value.items()}
            for query, value in raw["queries"].items()
            if isinstance(value, dict)
        }
    if isinstance(raw, dict) and "query" in raw and "conditions" in raw and isinstance(raw["conditions"], dict):
        return {str(raw["query"]): {str(k): bool(v) for k, v in raw["conditions"].items()}}
    return {}


def codex_conditions_for(query: str, conditions_by_query: dict[str, dict[str, bool]]) -> dict[str, bool]:
    if query in conditions_by_query:
        return conditions_by_query[query]
    query_terms = set(terms(query))
    best: tuple[int, dict[str, bool]] = (0, {})
    for candidate, conditions in conditions_by_query.items():
        overlap = len(query_terms & set(terms(candidate)))
        if overlap > best[0]:
            best = (overlap, conditions)
    return best[1] if best[0] > 0 else {}


def script_conditions(rag: dict[str, Any], selected_files: list[dict[str, Any]]) -> dict[str, bool]:
    scores = [float(entry.get("score", 0.0) or 0.0) for entry in rag.get("results", [])]
    score_margin_lt_20 = False
    if len(scores) >= 2 and scores[0] > 0:
        score_margin_lt_20 = ((scores[0] - scores[1]) / scores[0]) < 0.20
    return {
        "hit_conflict": any(item.get("layer") == "50_Conflicts" for item in selected_files),
        "hit_limited": any(item.get("layer") == "60_Limited_Rules" for item in selected_files),
        "no_final_rule": not any(item.get("layer") == "40_Final_Generalized_Rules" for item in selected_files),
        "score_margin_lt_20_pct": score_margin_lt_20,
        "low_evidence_support": False,
    }


def score_evidence_decision(script: dict[str, bool], codex: dict[str, bool], threshold: int) -> dict[str, Any]:
    combined = {**script, **codex}
    contributions = {
        name: weight
        for name, weight in EVIDENCE_SCORE_WEIGHTS.items()
        if combined.get(name)
    }
    score = sum(contributions.values())
    return {
        "threshold": threshold,
        "score": score,
        "should_expand_to_20": score >= threshold,
        "script_conditions": script,
        "codex_conditions": codex,
        "contributions": contributions,
    }


def retrieve_once(
    query: str,
    *,
    phase: str | None,
    layers: list[str],
    limit: int,
    candidate_limit: int,
    include_related: bool,
    workflow_limit: int,
) -> dict[str, Any]:
    effective_limit = max(1, workflow_limit) if layers == WORKFLOW_LAYERS else limit
    notes = load_notes(layers)
    by_id = {note.kid: note for note in notes}
    baseline_tokens = sum(estimate_tokens(note.text) for note in notes)
    search_result = build_search_result(query, notes, phase, candidate_limit)
    rag = rag_response(search_result, _SummaryStore(notes), query=query, phase=phase, limit=effective_limit)
    selected_ids = selected_note_ids(rag, effective_limit, include_related=include_related)
    selected_notes = [by_id[kid] for kid in selected_ids if kid in by_id]
    selected_full_tokens = sum(estimate_tokens(note.text) for note in selected_notes)
    rag_tokens = int(rag.get("total_tokens", 0)) + selected_full_tokens
    saved = max(0, baseline_tokens - rag_tokens)
    saved_pct = round((saved / baseline_tokens * 100.0), 2) if baseline_tokens else 0.0
    selected_files = [
        {
            "id": note.kid,
            "path": note.rel,
            "layer": note.layer,
            "title": note.title,
            "tokens": estimate_tokens(note.text),
            "outgoing_links": note.links,
            "incoming_links": note.incoming,
        }
        for note in selected_notes
    ]
    return {
        "query": query,
        "phase": phase or "",
        "limit": effective_limit,
        "layers": layers,
        "baseline_file_count": len(notes),
        "baseline_tokens": baseline_tokens,
        "rag_summary_tokens": int(rag.get("total_tokens", 0)),
        "selected_full_file_count": len(selected_notes),
        "selected_full_tokens": selected_full_tokens,
        "rag_total_tokens": rag_tokens,
        "tokens_saved": saved,
        "tokens_saved_pct": saved_pct,
        "rag": rag,
        "selected_files": selected_files,
    }


def run_query(
    query: str,
    *,
    phase: str | None,
    limit: int,
    candidate_limit: int,
    include_evidence: bool,
    include_workflow: bool | None,
    include_related: bool,
    workflow_limit: int,
    auto_evidence: bool,
    codex_conditions: dict[str, bool],
    evidence_threshold: int,
) -> dict[str, Any]:
    base_layers = allowed_layers(query, phase, False, include_workflow)
    if include_evidence:
        layers = allowed_layers(query, phase, True, include_workflow)
        result = retrieve_once(
            query,
            phase=phase,
            layers=layers,
            limit=limit,
            candidate_limit=candidate_limit,
            include_related=include_related,
            workflow_limit=workflow_limit,
        )
        result["evidence_decision"] = {
            "mode": "forced_include_evidence",
            "should_expand_to_20": True,
        }
        return result

    initial = retrieve_once(
        query,
        phase=phase,
        layers=base_layers,
        limit=limit,
        candidate_limit=candidate_limit,
        include_related=include_related,
        workflow_limit=workflow_limit,
    )
    decision = score_evidence_decision(
        script_conditions(initial["rag"], initial["selected_files"]),
        codex_conditions,
        evidence_threshold,
    )
    if base_layers == WORKFLOW_LAYERS:
        initial["evidence_decision"] = decision | {
            "mode": "workflow_route_no_20",
            "should_expand_to_20": False,
        }
        return initial
    if auto_evidence and decision["should_expand_to_20"] and base_layers != WORKFLOW_LAYERS:
        expanded = retrieve_once(
            query,
            phase=phase,
            layers=base_layers + EVIDENCE_LAYERS,
            limit=limit,
            candidate_limit=candidate_limit,
            include_related=include_related,
            workflow_limit=workflow_limit,
        )
        expanded["evidence_decision"] = decision | {"mode": "auto_expanded_to_20"}
        return expanded
    initial["evidence_decision"] = decision | {"mode": "not_expanded"}
    return initial


def render_report(results: list[dict[str, Any]]) -> str:
    total_baseline = sum(item["baseline_tokens"] for item in results)
    total_rag = sum(item["rag_total_tokens"] for item in results)
    saved = max(0, total_baseline - total_rag)
    saved_pct = round((saved / total_baseline * 100.0), 2) if total_baseline else 0.0
    lines = [
        "---",
        "title: KB RAG token savings latest",
        f"created: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "tags:",
        "  - layer/output",
        "  - kb-rag",
        "  - token-savings",
        "---",
        "",
        "# KB RAG Token Savings",
        "",
        "## Summary",
        "",
        f"- Queries: `{len(results)}`",
        f"- Baseline tokens: `{total_baseline}`",
        f"- RAG tokens: `{total_rag}`",
        f"- Tokens saved: `{saved}`",
        f"- Savings: `{saved_pct}%`",
        "",
        "## Method",
        "",
        "- Baseline loads every Markdown note from the allowed knowledge-base layers.",
        "- RAG first returns compact summaries, then selectively loads only chosen primary full vault notes.",
        "- `related_ids` are retained as optional follow-up links but are not loaded by default.",
        "- Token counts are estimated as `len(text) // 4`, matching the local recall-mode approximation.",
        "- Workflow governance is excluded from paper-writing queries and routed to `35_Workflow_Governance` only for workflow/governance queries.",
        "- Optional writing-time evidence expansion stops at `20_Paper_Memories`; `10_Project_Change_Log` is not loaded during writing retrieval.",
        "",
        "## Query Results",
        "",
    ]
    for item in results:
        lines += [
            f"### {item['query']}",
            "",
            f"- Phase: `{item['phase'] or 'none'}`",
            f"- Selected limit: `{item['limit']}`",
            f"- Layers: `{', '.join(item['layers'])}`",
            f"- Baseline: `{item['baseline_file_count']}` files, `{item['baseline_tokens']}` tokens",
            f"- RAG: summaries `{item['rag_summary_tokens']}` + selected full `{item['selected_full_tokens']}` = `{item['rag_total_tokens']}` tokens",
            f"- Saved: `{item['tokens_saved']}` tokens (`{item['tokens_saved_pct']}%`)",
            f"- Evidence decision: `{item.get('evidence_decision', {}).get('mode', 'none')}` | score `{item.get('evidence_decision', {}).get('score', '')}` / threshold `{item.get('evidence_decision', {}).get('threshold', '')}`",
            "- Selected files:",
        ]
        for selected in item["selected_files"]:
            lines.append(f"  - `{selected['path']}` | `{selected['tokens']}` tokens")
            if selected.get("outgoing_links") or selected.get("incoming_links"):
                outgoing = ", ".join(selected.get("outgoing_links") or []) or "none"
                incoming = ", ".join(selected.get("incoming_links") or []) or "none"
                lines.append(f"    - links out: `{outgoing}`")
                lines.append(f"    - links in: `{incoming}`")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", action="append", help="Query to run. May be repeated.")
    parser.add_argument("--phase", default="", help="Optional phase tag to boost.")
    parser.add_argument("--limit", type=int, default=3)
    parser.add_argument("--workflow-limit", type=int, default=1)
    parser.add_argument("--candidate-limit", type=int, default=20)
    parser.add_argument("--include-evidence", action="store_true")
    parser.add_argument("--include-workflow", action="store_true")
    parser.add_argument("--exclude-workflow", action="store_true")
    parser.add_argument("--include-related", action="store_true")
    parser.add_argument("--auto-evidence", action="store_true")
    parser.add_argument("--codex-conditions", default=str(DEFAULT_CODEX_CONDITIONS))
    parser.add_argument("--evidence-threshold", type=int, default=3)
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()

    queries = args.query or [
        "摘要开头 界面波 金属间化合物 厚度",
        "引言 文献综述 实验 模拟 差距",
        "工作流 论文要求 混淆",
    ]
    include_workflow: bool | None
    if args.include_workflow:
        include_workflow = True
    elif args.exclude_workflow:
        include_workflow = False
    else:
        include_workflow = None

    conditions_by_query = load_codex_conditions(Path(args.codex_conditions) if args.codex_conditions else None)
    results = [
        run_query(
            query,
            phase=args.phase or None,
            limit=args.limit,
            candidate_limit=args.candidate_limit,
            include_evidence=args.include_evidence,
            include_workflow=include_workflow,
            include_related=args.include_related,
            workflow_limit=args.workflow_limit,
            auto_evidence=args.auto_evidence,
            codex_conditions=codex_conditions_for(query, conditions_by_query),
            evidence_threshold=args.evidence_threshold,
        )
        for query in queries
    ]
    report = render_report(results)
    if args.write_report:
        ITER_DIR.mkdir(parents=True, exist_ok=True)
        (ITER_DIR / "kb_rag_token_savings_latest.md").write_text(report, encoding="utf-8-sig")
    print(json.dumps({"results": results, "report": report}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
