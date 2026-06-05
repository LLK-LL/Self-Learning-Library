from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
import sqlite3
import zipfile
from dataclasses import dataclass
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "paper_writing_obsidian_vault"
ITER_DIR = VAULT / "70_Iterative_Thinking"
MEMORY_DIR = VAULT / "20_Paper_Memories"
CHANGE_DIR = VAULT / "10_Project_Change_Log"
RULE_DIR = VAULT / "30_Writing_Rules"
PROCESS_DIR = VAULT / "35_Workflow_Governance"
CONFLICT_DIR = VAULT / "50_Conflicts"
LIMITED_DIR = VAULT / "60_Limited_Rules"
FINAL_RULE_DIR = VAULT / "40_Final_Generalized_Rules"
SUPERVISION_DIR = VAULT / "45_Supervision"
LEGACY_CHANGE_DIR = VAULT / "10_修改点"
LEGACY_RULE_DIR = VAULT / "20_提炼"
EXPORT_DIR = ROOT / "memory_exports" / "paper_writing"
NON_PAPER_EXPORT_DIR = ROOT / "memory_exports" / "non_paper"
LATEST_JSON = ITER_DIR / "conclusions_latest.json"
CANDIDATE_RULES_JSON = ITER_DIR / "codex_candidate_rules.json"
IMPORT_INDEX = VAULT / ".paper_memory_import_index.json"
MEMORY_DB = Path(r"C:\Users\Administrator\.tam\memory.db")
PROJECT_KEY = "Ti-Al explosive welding SPH-FEM analysis"
SCI_MEMORY_SKILL = Path(r"C:\Users\Administrator\.codex\skills\SCI-memory\SKILL.md")
SKILL_RULES_START = "<!-- AUTO-GENERATED FINAL RULES START -->"
SKILL_RULES_END = "<!-- AUTO-GENERATED FINAL RULES END -->"


PAPER_TAGS = {
    "paper-writing",
    "abstract",
    "writing-style",
    "TC4-Al6061",
    "SPH-FEM",
    "introduction",
    "references",
    "revision-process",
    "conflict-detection",
    "writing-rule",
}

NON_PAPER_TAGS = {
    "skill",
    "codex-skill",
    "SCI-memory",
    "sci-memory",
    "coding",
    "programming",
    "code",
    "codex-automation",
    "manual-run",
    "memory-import",
    "knowledge-base-structure",
    "obsidian",
}

PAPER_TERMS = {
    "paper",
    "manuscript",
    "abstract",
    "introduction",
    "references",
    "citation",
    "literature",
    "writing",
    "revision",
    "sci",
    "tc4/al6061",
    "tc4-al6061",
    "al3ti",
    "sph-fem",
}

NON_PAPER_TERMS = {
    "codex skill",
    "skill folder",
    "quick_validate",
    "tools/paper_iteration.py",
    "run_paper_iteration.ps1",
    "automation id",
    "obsidian knowledge base",
    "knowledge base structure",
    "memory import",
    "script",
    "programming",
    "coding",
}


TITLE_BY_ID = {
    25: "Abstract rule - earlier industry background constraint",
    26: "Abstract rule - direct opening superseded version",
    27: "Abstract rule - predict layer thickness and distribution",
    28: "Abstract rule - interface wave as validation only",
    31: "Abstract final rule - intermetallic layer thickness and distribution",
    34: "Introduction revision - references and second paragraph structure",
    35: "Paper memory export path convention",
}


@dataclass
class EvidenceFile:
    path: Path
    sha256: str
    modified: str
    text: str


@dataclass
class VaultNode:
    stem: str
    path: Path
    folder: str
    tags: list[str]
    links: list[str]
    layer: str


def write_utf8(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8-sig")


def read_docx(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        xml = archive.read("word/document.xml").decode("utf-8", errors="replace")
    paras = re.findall(r"<w:p[\s\S]*?</w:p>", xml)
    out: list[str] = []
    for para in paras:
        runs = re.findall(r"<w:t[^>]*>([\s\S]*?)</w:t>", para)
        if runs:
            out.append(html.unescape("".join(runs)))
    return "\n".join(out)


def read_text(path: Path) -> str:
    for enc in ("utf-8-sig", "utf-8", "gb18030"):
        try:
            return path.read_text(encoding=enc, errors="strict")
        except UnicodeError:
            continue
    return path.read_text(encoding="utf-8", errors="replace")


def parse_frontmatter_tags(text: str) -> list[str]:
    fields = parse_frontmatter_fields(text)
    raw_tags = fields.get("tags", [])
    return sorted(set(raw_tags if isinstance(raw_tags, list) else []))


def parse_frontmatter_fields(text: str) -> dict:
    match = re.match(r"^---\s*\n([\s\S]*?)\n---\s*\n", text)
    if not match:
        return {}
    fields: dict[str, str | list[str]] = {}
    tags: list[str] = []
    lines = match.group(1).splitlines()
    active_list_key: str | None = None
    for line in lines:
        key_value = re.match(r"^([A-Za-z_][\w-]*):\s*(.*?)\s*$", line)
        if key_value:
            key = key_value.group(1).strip()
            value = key_value.group(2).strip()
            active_list_key = key if value == "" else None
            if value:
                fields[key] = value.strip("\"'")
                if key == "tags":
                    tags.extend(tag.strip().strip("\"'") for tag in value.split(",") if tag.strip())
            elif key == "tags":
                fields[key] = tags
            continue
        if active_list_key:
            item = re.match(r"^\s*-\s*(.+?)\s*$", line)
            if item:
                value = item.group(1).strip().strip("\"'")
                if active_list_key == "tags":
                    tags.append(value)
                else:
                    current = fields.setdefault(active_list_key, [])
                    if isinstance(current, list):
                        current.append(value)
    if tags:
        fields["tags"] = sorted(set(tags))
    return fields


def parse_wikilinks(text: str) -> list[str]:
    links: list[str] = []
    for raw in re.findall(r"\[\[([^\]]+)\]\]", text):
        target = raw.split("|", 1)[0].split("#", 1)[0].strip()
        if target:
            links.append(Path(target).stem)
    return sorted(set(links))


def vault_layer(rel: Path) -> str:
    folder = rel.parent.as_posix()
    if folder in {"20_Paper_Memories", "10_Project_Change_Log"}:
        return "evidence"
    if folder in {"30_Writing_Rules", "35_Workflow_Governance", "40_Final_Generalized_Rules", "45_Supervision", "50_Conflicts", "60_Limited_Rules"}:
        return "reasoning"
    return "output"


def layer_tag(layer: str) -> str:
    return f"layer/{layer}"


def replace_frontmatter_tags(text: str, tags: list[str]) -> str:
    tag_lines = ["tags:"] + [f"  - {tag}" for tag in sorted(set(tags))]
    tag_block = "\n".join(tag_lines)
    match = re.match(r"^---\s*\n([\s\S]*?)\n---\s*\n?", text)
    if not match:
        return f"---\n{tag_block}\n---\n\n{text}"

    frontmatter_text = match.group(1)
    lines = frontmatter_text.splitlines()
    out: list[str] = []
    idx = 0
    replaced = False
    while idx < len(lines):
        line = lines[idx]
        if line.startswith("tags:"):
            out.extend(tag_lines)
            replaced = True
            idx += 1
            while idx < len(lines) and (lines[idx].startswith(" ") or lines[idx].startswith("\t") or lines[idx].strip() == ""):
                idx += 1
            continue
        out.append(line)
        idx += 1
    if not replaced:
        out.extend(tag_lines)
    body = text[match.end():]
    return "---\n" + "\n".join(out).rstrip() + "\n---\n\n" + body.lstrip("\n")


def ensure_vault_layer_tags() -> int:
    if not VAULT.exists():
        return 0
    changed = 0
    for path in sorted(VAULT.rglob("*.md")):
        if ".obsidian" in path.parts:
            continue
        rel = path.relative_to(VAULT)
        current = read_text(path)
        tags = [tag for tag in parse_frontmatter_tags(current) if not tag.startswith("layer/")]
        tags.append(layer_tag(vault_layer(rel)))
        updated = replace_frontmatter_tags(current, tags)
        if updated != current:
            write_utf8(path, updated)
            changed += 1
    return changed


def should_skip_file(path: Path) -> bool:
    parts = set(path.parts)
    name = path.name
    if name.startswith("~") or name.endswith(".tmp"):
        return True
    if ".obsidian" in parts:
        return True
    if "70_Iterative_Thinking" in parts:
        return True
    if "non_paper" in parts:
        return True
    if path.suffix.lower() not in {".docx", ".md", ".txt", ".json"}:
        return True
    return False


def collect_workspace_evidence(root: Path) -> list[EvidenceFile]:
    files: list[EvidenceFile] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or should_skip_file(path):
            continue
        try:
            raw = path.read_bytes()
            digest = hashlib.sha256(raw).hexdigest()
            text = read_docx(path) if path.suffix.lower() == ".docx" else read_text(path)
        except Exception as exc:
            digest = ""
            text = f"[READ_ERROR] {type(exc).__name__}: {exc}"
        files.append(
            EvidenceFile(
                path=path.relative_to(root),
                sha256=digest,
                modified=datetime.fromtimestamp(path.stat().st_mtime).isoformat(timespec="seconds"),
                text=text,
            )
        )
    return files


def build_incoming(nodes: dict[str, VaultNode], allowed_layers: set[str] | None = None) -> dict[str, list[str]]:
    incoming: dict[str, list[str]] = {stem: [] for stem in nodes}
    for source, node in nodes.items():
        if allowed_layers is not None and node.layer not in allowed_layers:
            continue
        for target in node.links:
            target_node = nodes.get(target)
            if not target_node:
                continue
            if allowed_layers is not None and target_node.layer not in allowed_layers:
                continue
            incoming[target].append(source)
    for sources in incoming.values():
        sources.sort()
    return incoming


def collect_vault_graph() -> dict:
    nodes: dict[str, VaultNode] = {}
    if not VAULT.exists():
        return {"nodes": {}, "incoming": {}, "evidence_incoming": {}, "orphans": [], "evidence_orphans": []}
    for path in sorted(VAULT.rglob("*.md")):
        if ".obsidian" in path.parts:
            continue
        text = read_text(path)
        rel = path.relative_to(VAULT)
        nodes[path.stem] = VaultNode(
            stem=path.stem,
            path=rel,
            folder=rel.parent.as_posix(),
            tags=parse_frontmatter_tags(text),
            links=parse_wikilinks(text),
            layer=vault_layer(rel),
        )
    incoming = build_incoming(nodes)
    evidence_incoming = build_incoming(nodes, {"evidence"})
    orphans = sorted(stem for stem, node in nodes.items() if not node.links and not incoming.get(stem))
    evidence_orphans = sorted(
        stem
        for stem, node in nodes.items()
        if node.layer == "evidence"
        and not [link for link in node.links if nodes.get(link) and nodes[link].layer == "evidence"]
        and not evidence_incoming.get(stem)
    )
    return {
        "nodes": nodes,
        "incoming": incoming,
        "evidence_incoming": evidence_incoming,
        "orphans": orphans,
        "evidence_orphans": evidence_orphans,
    }


def graph_node_summary(stem: str, graph: dict, evidence_only: bool = False) -> dict:
    node = graph["nodes"].get(stem)
    incoming = graph["evidence_incoming" if evidence_only else "incoming"].get(stem, [])
    if not node:
        return {
            "note": stem,
            "folder": "",
            "layer": "",
            "tags": [],
            "outgoing_links": [],
            "incoming_links": [],
            "relation_score": 0,
        }
    outgoing = [
        link for link in node.links
        if not evidence_only or (graph["nodes"].get(link) and graph["nodes"][link].layer == "evidence")
    ]
    return {
        "note": stem,
        "folder": node.folder,
        "layer": node.layer,
        "tags": node.tags,
        "outgoing_links": outgoing,
        "incoming_links": incoming,
        "relation_score": len(outgoing) + len(incoming) if node.layer == "evidence" or not evidence_only else 0,
    }


def attach_graph_support(conclusions: list[dict], conflicts: list[dict], graph: dict) -> None:
    for item in conclusions:
        memory_nodes = [graph_node_summary(note_link(mem), graph, evidence_only=True) for mem in item["memory_evidence"]]
        rule_node = graph_node_summary(item["title"], graph)
        graph_score = sum(node["relation_score"] for node in memory_nodes)
        mentor_evidence = sum(1 for mem in item["memory_evidence"] if mem.get("priority_score", 0) >= 100)
        item["graph_support"] = {
            "rule_node": rule_node,
            "memory_nodes": memory_nodes,
            "supporting_memory_count": len(memory_nodes),
            "mentor_evidence_count": mentor_evidence,
            "graph_relation_score": graph_score,
            "scoring_layer": "evidence",
            "isolated_memory_notes": [node["note"] for node in memory_nodes if node["relation_score"] == 0],
        }

    for conflict in conflicts:
        conflict_node = graph_node_summary(conflict["topic"], graph)
        memory_nodes = [graph_node_summary(note_link(record), graph, evidence_only=True) for record in conflict["records"]]
        conflict["graph_support"] = {
            "conflict_node": conflict_node,
            "memory_nodes": memory_nodes,
            "graph_relation_score": sum(node["relation_score"] for node in memory_nodes),
            "scoring_layer": "evidence",
        }


def render_graph_analysis(graph: dict, conclusions: list[dict], conflicts: list[dict], layer_tag_updates: int) -> str:
    nodes: dict[str, VaultNode] = graph["nodes"]
    folder_counts: dict[str, int] = {}
    layer_counts: dict[str, int] = {}
    for node in nodes.values():
        folder_counts[node.folder] = folder_counts.get(node.folder, 0) + 1
        layer_counts[node.layer] = layer_counts.get(node.layer, 0) + 1
    central = sorted(
        (graph_node_summary(stem, graph) for stem in nodes),
        key=lambda item: (-item["relation_score"], item["note"]),
    )[:12]
    evidence_central = sorted(
        (graph_node_summary(stem, graph, evidence_only=True) for stem, node in nodes.items() if node.layer == "evidence"),
        key=lambda item: (-item["relation_score"], item["note"]),
    )[:12]

    lines = [
        "---",
        "title: Vault graph analysis latest",
        f"created: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "tags:",
        "  - layer/output",
        "  - paper-iteration",
        "  - vault-graph",
        "---",
        "",
        "# Vault Graph Analysis",
        "",
        "## Scope",
        "",
        "- This analysis is built from Markdown frontmatter tags and `[[wikilinks]]` in the vault.",
        "- It does not call Obsidian CLI or the Obsidian application.",
        "- The vault graph is separated into evidence, reasoning, and output layers.",
        "- Only the evidence layer contributes to conclusion support scores.",
        "- Reasoning and output layers are reported for navigation and audit only.",
        "",
        "## Vault Coverage",
        "",
        f"- Markdown notes: `{len(nodes)}`",
        f"- Isolated notes: `{len(graph['orphans'])}`",
        f"- Evidence-layer isolated notes: `{len(graph['evidence_orphans'])}`",
        f"- Layer tag updates this run: `{layer_tag_updates}`",
        "",
    ]
    lines += ["## Layer Counts", ""]
    for layer in ("evidence", "reasoning", "output"):
        lines.append(f"- `{layer}`: `{layer_counts.get(layer, 0)}` notes")

    lines += ["", "## Folder Counts", ""]
    for folder, count in sorted(folder_counts.items()):
        lines.append(f"- `{folder or '.'}`: `{count}` notes")

    lines += ["", "## Most Connected Evidence Notes", ""]
    for item in evidence_central:
        lines.append(
            f"- [[{item['note']}]] | evidence score `{item['relation_score']}` | "
            f"in `{len(item['incoming_links'])}` | out `{len(item['outgoing_links'])}`"
        )

    lines += ["", "## Most Connected Notes Across All Layers", ""]
    for item in central:
        lines.append(
            f"- [[{item['note']}]] | layer `{item['layer']}` | score `{item['relation_score']}` | "
            f"in `{len(item['incoming_links'])}` | out `{len(item['outgoing_links'])}`"
        )

    lines += ["", "## Conclusion Graph Support", ""]
    for item in conclusions:
        support = item.get("graph_support", {})
        lines += [
            f"### {item['id']} {item['title']}",
            "",
            f"- Evidence graph relation score: `{support.get('graph_relation_score', 0)}`",
            f"- Supporting memory notes: `{support.get('supporting_memory_count', 0)}`",
            f"- Mentor-priority evidence notes: `{support.get('mentor_evidence_count', 0)}`",
            "- Reasoning and output nodes do not contribute to this score.",
        ]
        isolated = support.get("isolated_memory_notes") or []
        if isolated:
            lines.append(f"- Structurally isolated evidence: {', '.join(f'[[{note}]]' for note in isolated)}")
        lines.append("")

    lines += ["## Conflict Graph Support", ""]
    if conflicts:
        for conflict in conflicts:
            support = conflict.get("graph_support", {})
            lines += [
                f"### {conflict['topic']}",
                "",
                f"- Evidence graph relation score: `{support.get('graph_relation_score', 0)}`",
                "",
            ]
    else:
        lines.append("- No conflicts detected.")
    return "\n".join(lines)


def load_all_memory_records() -> list[dict]:
    if not MEMORY_DB.exists():
        return []
    conn = sqlite3.connect(MEMORY_DB)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """
        SELECT id, session_id, type, content, context, project, tags, status,
               superseded_by, confidence, source, created_at, last_confirmed,
               recall_count, last_recalled, branch, agent_id, parent_agent_id,
               importance
        FROM knowledge
        ORDER BY created_at ASC, id ASC
        """
    ).fetchall()
    conn.close()

    records: list[dict] = []
    for row in rows:
        item = dict(row)
        try:
            item["tags"] = json.loads(item.get("tags") or "[]")
        except Exception:
            item["tags"] = []
        records.append(item)
    return records


def classify_memory(record: dict) -> str:
    project = record.get("project") or ""
    content = record.get("content") or ""
    context = record.get("context") or ""
    tags = set(record.get("tags") or [])
    hay = "\n".join([project, content, context, " ".join(tags)]).lower()

    if bool(tags & {"github", "download", "windows-exe", "codex-provider-sync"}) or any(
        term in hay
        for term in ("downloaded", "windows executable", ".exe", "github project", "release metadata")
    ):
        return "other"

    manuscript_signal = any(
        term in hay
        for term in (
            "abstract",
            "introduction",
            "references",
            "citation",
            "manuscript",
            "literature review",
            "paper revision",
            "paper-writing-related",
            "tc4/al6061",
            "tc4-al6061",
            "al3ti",
        )
    )

    if "skill" in hay or "sci-memory" in hay or "codex-skill" in hay or bool(tags & {"skill", "codex-skill", "SCI-memory", "sci-memory"}):
        return "skills"
    if "automation" in hay or "run_paper_iteration" in hay or "paper_iteration.py" in hay:
        return "automation"
    if "obsidian vault" in hay or "knowledge base" in hay or "paper_writing_obsidian_vault" in hay:
        return "automation"
    if manuscript_signal:
        return "paper"
    if "code" in hay or "coding" in hay or "script" in hay or ".py" in hay or ".ps1" in hay:
        return "coding"

    paper_signal = (
        bool(tags & PAPER_TAGS)
        or any(term in hay for term in ("abstract", "introduction", "citation", "references", "al3ti"))
    )

    non_paper_signal = bool(tags & NON_PAPER_TAGS) or any(term in hay for term in NON_PAPER_TERMS)
    if paper_signal and not non_paper_signal:
        return "paper"
    return "other"


def load_memory_records() -> tuple[list[dict], dict[str, list[dict]]]:
    all_records = load_all_memory_records()
    paper_records: list[dict] = []
    non_paper: dict[str, list[dict]] = {"skills": [], "coding": [], "automation": [], "other": []}
    for item in all_records:
        category = classify_memory(item)
        if category == "paper":
            paper_records.append(item)
        else:
            non_paper.setdefault(category, []).append(item)
    return paper_records, non_paper


def sanitize_filename(text: str, fallback: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "", text)
    text = text.strip(". ")
    return (text or fallback)[:96]


def memory_title(record: dict) -> str:
    rid = int(record.get("id") or -1)
    if rid in TITLE_BY_ID:
        return TITLE_BY_ID[rid]
    content = (record.get("content") or "").strip()
    sentence = re.split(r"(?<=[.!?。！？])\s+", content)[0]
    return sanitize_filename(sentence, f"Paper memory {rid}")


def frontmatter(title: str, tags: list[str]) -> str:
    tag_text = "\n".join(f"  - {tag}" for tag in sorted(set(tags)))
    return (
        "---\n"
        f"title: {title}\n"
        f"created: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        "tags:\n"
        f"{tag_text}\n"
        "---\n\n"
    )


def import_memories(records: list[dict]) -> list[dict]:
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    for old in MEMORY_DIR.glob("*.md"):
        old.unlink()

    imported: list[dict] = []
    used: set[str] = set()
    index = {"records": {}}
    for record in records:
        rid = str(record.get("id"))
        base = memory_title(record)
        title = sanitize_filename(base, f"Paper memory {rid}")
        if title in used:
            title = sanitize_filename(f"{title} - memory {rid}", f"Paper memory {rid}")
        used.add(title)
        filename = f"{title}.md"
        record = {**record, "note_title": title, "note_file": filename, "changed": True}
        imported.append(record)

        note = frontmatter(title, ["paper-memory", f"memory-id-{rid}", str(record.get("type") or "memory")])
        note += f"# {title}\n\n"
        note += "## Source Metadata\n\n"
        note += f"- Memory ID: `{rid}`\n"
        note += f"- Type: `{record.get('type') or ''}`\n"
        note += f"- Status: `{record.get('status') or ''}`\n"
        note += f"- Project: `{record.get('project') or ''}`\n"
        note += f"- Created: `{record.get('created_at') or ''}`\n"
        note += f"- Importance: `{record.get('importance') or ''}`\n"
        if record.get("superseded_by"):
            note += f"- Superseded by memory: `{record.get('superseded_by')}`\n"
        note += "\n## Memory Content\n\n"
        note += (record.get("content") or "") + "\n"
        if record.get("context"):
            note += "\n## Context\n\n" + (record.get("context") or "") + "\n"
        write_utf8(MEMORY_DIR / filename, note)
        index["records"][rid] = {"title": title, "file": filename}

    write_utf8(IMPORT_INDEX, json.dumps(index, ensure_ascii=False, indent=2))
    return imported


def load_existing_paper_memory_notes() -> list[dict]:
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    records: list[dict] = []
    for path in sorted(MEMORY_DIR.glob("*.md")):
        text = read_text(path)
        fm = parse_frontmatter_fields(text)
        title_match = re.search(r"^title:\s*(.+)$", text, flags=re.MULTILINE)
        id_match = re.search(r"^- Memory ID:\s*`?([^`\n]+)`?", text, flags=re.MULTILINE)
        type_match = re.search(r"^- Type:\s*`?([^`\n]+)`?", text, flags=re.MULTILINE)
        status_match = re.search(r"^- Status:\s*`?([^`\n]+)`?", text, flags=re.MULTILINE)
        importance_match = re.search(r"^- Importance:\s*`?([^`\n]+)`?", text, flags=re.MULTILINE)
        source_match = re.search(r"^- Source:\s*`?([^`\n]+)`?", text, flags=re.MULTILINE)
        priority_match = re.search(r"^- Source Priority:\s*`?([^`\n]+)`?", text, flags=re.MULTILINE)
        content_match = re.search(r"## Memory Content\s+([\s\S]*?)(?:\n## |\Z)", text)
        context_match = re.search(r"## Context\s+([\s\S]*?)(?:\n## |\Z)", text)
        title = sanitize_filename((str(fm.get("title") or "").strip() or (title_match.group(1).strip() if title_match else path.stem)), path.stem)
        rid_raw = id_match.group(1).strip() if id_match else path.stem
        try:
            rid: int | str = int(rid_raw)
        except Exception:
            rid = rid_raw
        records.append(
            {
                "id": rid,
                "type": type_match.group(1).strip() if type_match else "memory-note",
                "status": str(fm.get("status") or (status_match.group(1).strip() if status_match else "active")),
                "importance": str(fm.get("importance") or fm.get("priority") or (importance_match.group(1).strip() if importance_match else "")),
                "source": str(fm.get("source") or (source_match.group(1).strip() if source_match else "")),
                "source_priority": str(fm.get("source_priority") or fm.get("source-priority") or fm.get("priority") or (priority_match.group(1).strip() if priority_match else "")),
                "scope": fm.get("scope") or fm.get("application_scope") or fm.get("application-scope") or "",
                "project": PROJECT_KEY,
                "tags": ["paper-memory", "obsidian-existing"],
                "content": (content_match.group(1).strip() if content_match else text.strip()),
                "context": (context_match.group(1).strip() if context_match else ""),
                "note_title": title,
                "note_file": path.name,
                "changed": False,
            }
        )
    return records


def export_memory_snapshot(records: list[dict]) -> None:
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%dT%H%M%S")
    payload = {
        "exported_at": stamp,
        "source_db": str(MEMORY_DB),
        "count": len(records),
        "records": records,
    }
    json_text = json.dumps(payload, ensure_ascii=False, indent=2, default=str)
    write_utf8(EXPORT_DIR / f"paper_writing_memory_{stamp}.json", json_text)
    write_utf8(EXPORT_DIR / "paper_writing_memory_latest.json", json_text)

    lines = ["# Paper Writing Memory Export", "", f"- Exported at: `{stamp}`", f"- Records: `{len(records)}`", ""]
    for record in records:
        lines += [
            f"## {memory_title(record)}",
            "",
            f"- Memory ID: `{record.get('id')}`",
            f"- Type: `{record.get('type')}`",
            f"- Status: `{record.get('status')}`",
            "",
            record.get("content") or "",
            "",
        ]
    md = "\n".join(lines)
    write_utf8(EXPORT_DIR / f"paper_writing_memory_{stamp}.md", md)
    write_utf8(EXPORT_DIR / "paper_writing_memory_latest.md", md)


def export_non_paper_memory_snapshots(groups: dict[str, list[dict]]) -> None:
    stamp = datetime.now().strftime("%Y%m%dT%H%M%S")
    index_lines = [
        "# Non-paper Memory Export Index",
        "",
        "These records are intentionally excluded from the Obsidian paper-writing knowledge base.",
        "",
    ]
    for category, records in sorted(groups.items()):
        category_dir = NON_PAPER_EXPORT_DIR / category
        category_dir.mkdir(parents=True, exist_ok=True)
        payload = {
            "exported_at": stamp,
            "category": category,
            "source_db": str(MEMORY_DB),
            "count": len(records),
            "records": records,
        }
        json_text = json.dumps(payload, ensure_ascii=False, indent=2, default=str)
        write_utf8(category_dir / f"{category}_memory_{stamp}.json", json_text)
        write_utf8(category_dir / f"{category}_memory_latest.json", json_text)

        lines = [
            f"# {category.title()} Memory Export",
            "",
            f"- Exported at: `{stamp}`",
            f"- Records: `{len(records)}`",
            "",
        ]
        for record in records:
            lines += [
                f"## {memory_title(record)}",
                "",
                f"- Memory ID: `{record.get('id')}`",
                f"- Type: `{record.get('type')}`",
                f"- Status: `{record.get('status')}`",
                f"- Project: `{record.get('project')}`",
                "",
                record.get("content") or "",
                "",
            ]
        md = "\n".join(lines)
        write_utf8(category_dir / f"{category}_memory_{stamp}.md", md)
        write_utf8(category_dir / f"{category}_memory_latest.md", md)
        index_lines.append(f"- `{category}`: `{len(records)}` records -> `{category_dir}`")
    write_utf8(NON_PAPER_EXPORT_DIR / "index.md", "\n".join(index_lines) + "\n")


def has(record: dict, *terms: str) -> bool:
    text = "\n".join(
        [
            record.get("content") or "",
            record.get("context") or "",
            " ".join(record.get("tags") or []),
        ]
    ).lower()
    return all(term.lower() in text for term in terms)


def is_workflow_governance_record(record: dict) -> bool:
    tags = {str(tag).lower() for tag in (record.get("tags") or [])}
    text = "\n".join(
        [
            record.get("note_title") or "",
            record.get("note_file") or "",
            record.get("content") or "",
            record.get("context") or "",
            " ".join(record.get("tags") or []),
        ]
    ).lower()
    return bool(tags & {"workflow-governance", "knowledge-base-structure"}) or any(
        term in text
        for term in (
            "35_workflow_governance",
            "workflow governance",
            "process-governance",
            "process governance",
            "knowledge-base maintenance",
            "工作流",
            "论文要求",
        )
    )


def source_priority_score(record: dict) -> int:
    source = (record.get("source") or "").lower()
    priority = (record.get("source_priority") or "").lower()
    importance = (record.get("importance") or "").lower()
    status = (record.get("status") or "").lower()
    tags = " ".join(str(tag) for tag in (record.get("tags") or [])).lower()
    text = "\n".join([source, priority, importance, status, tags, record.get("content") or "", record.get("context") or ""]).lower()
    if "mentor_high" in priority or "mentor" in source or "导师" in text:
        return 300
    if ("supervision" in priority or "supervision" in source or "supervision" in tags) and status != "inactive":
        return 240
    if "user_confirmed" in priority or "user-confirmed" in tags or "user_confirmation" in source:
        return 210
    if "user_decision" in priority or "user_high" in priority or source == "user" or "user_correction" in source:
        return 200
    if "reviewer" in source or "审稿" in text:
        return 180
    if "highest" in importance or "highest" in priority:
        return 170
    if importance == "high" or "priority/high" in tags:
        return 50
    if importance == "medium":
        return 20
    return 0


def sort_by_source_priority(records: list[dict]) -> list[dict]:
    return sorted(records, key=lambda record: (-source_priority_score(record), str(record.get("note_title") or "")))


def matching(records: list[dict], predicate, limit: int = 8, include_workflow_governance: bool = False) -> list[dict]:
    return sort_by_source_priority(
        [
            record
            for record in records
            if predicate(record) and (include_workflow_governance or not is_workflow_governance_record(record))
        ]
    )[:limit]


def mem_ref(record: dict) -> dict:
    return {
        "id": record.get("id"),
        "title": record.get("note_title") or memory_title(record),
        "file": record.get("note_file"),
        "content": record.get("content") or "",
        "source": record.get("source") or "",
        "source_priority": record.get("source_priority") or "",
        "scope": record.get("scope") or "",
        "priority_score": source_priority_score(record),
    }


def load_supervision_priority_notes() -> list[dict]:
    notes: list[dict] = []
    if not SUPERVISION_DIR.exists():
        return notes
    for path in sorted(SUPERVISION_DIR.glob("*.md")):
        if path.name == "README.md" or path.name.startswith("TEMPLATE"):
            continue
        text = read_text(path)
        fm = parse_frontmatter_fields(text)
        tags = fm.get("tags", [])
        tags_list = tags if isinstance(tags, list) else []
        title = str(fm.get("title") or path.stem)
        status = str(fm.get("status") or "active")
        priority = str(fm.get("priority") or fm.get("source_priority") or "")
        source = str(fm.get("source") or "supervision")
        raw_scope = fm.get("scope") or fm.get("application_scope") or fm.get("application-scope") or infer_scope_from_text(text, tags_list)
        scope = ", ".join(raw_scope) if isinstance(raw_scope, list) else str(raw_scope)
        record = {
            "id": path.stem,
            "title": title,
            "file": path.name,
            "note_title": title,
            "note_file": path.name,
            "content": text,
            "context": "",
            "source": source,
            "source_priority": priority or "supervision_high",
            "importance": priority,
            "status": status,
            "scope": scope,
            "tags": tags_list + ["supervision"],
        }
        if source_priority_score(record) >= 240 and status.lower() != "inactive":
            notes.append(record)
    return sort_by_source_priority(notes)


def infer_scope_from_text(text: str, tags: list[str]) -> str:
    hay = "\n".join([text, " ".join(tags)]).lower()
    scopes: list[str] = []
    if "abstract" in hay or "摘要" in hay:
        scopes.append("abstract")
    if "introduction" in hay or "引言" in hay:
        scopes.append("introduction")
    if "formula" in hay or "omml" in hay or "公式" in hay or "theory" in hay:
        scopes.append("theory-formula")
    if "docx" in hay or "word" in hay or "format" in hay or "格式" in hay:
        scopes.append("global-format")
    if "script" in hay or "脚本" in hay or "file" in hay or "文件" in hay:
        scopes.append("file-processing")
    if "workflow" in hay or "harness" in hay or "knowledge" in hay or "知识库" in hay:
        scopes.append("knowledge-base-governance")
    return ", ".join(dict.fromkeys(scopes)) or "unspecified"


def legacy_memory_link_map(imported: list[dict]) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for record in imported:
        rid = str(record.get("id"))
        stem = Path(record.get("note_file") or "").stem
        if not rid or not stem:
            continue
        mapping[f"Memory Record {rid}"] = stem
        mapping[f"Memory Record {rid} - {record.get('type') or 'memory'}"] = stem
    return mapping


def replace_legacy_memory_links(text: str, imported: list[dict]) -> str:
    mapping = legacy_memory_link_map(imported)
    for old, new in sorted(mapping.items(), key=lambda item: len(item[0]), reverse=True):
        text = text.replace(f"[[{old}]]", f"[[{new}]]")
    return text


def migrate_legacy_vault_content(imported: list[dict]) -> None:
    CHANGE_DIR.mkdir(parents=True, exist_ok=True)

    if LEGACY_CHANGE_DIR.exists():
        for old in CHANGE_DIR.glob("*.md"):
            old.unlink()
        for source in sorted(LEGACY_CHANGE_DIR.glob("*.md")):
            text = read_text(source)
            text = replace_legacy_memory_links(text, imported)
            text = text.replace("## 对应记忆", "## Evidence Memories")
            text = text.replace("# 论文记忆同步约定", "# Paper memory synchronization convention")
            write_utf8(CHANGE_DIR / source.name, text)
        shutil.rmtree(LEGACY_CHANGE_DIR)

    if LEGACY_RULE_DIR.exists():
        PROCESS_DIR.mkdir(parents=True, exist_ok=True)
        for source in sorted(LEGACY_RULE_DIR.glob("*.md")):
            text = read_text(source)
            text = replace_legacy_memory_links(text, imported)
            title = f"Legacy migrated - {source.stem}"
            target = PROCESS_DIR / f"{sanitize_filename(title, 'legacy-rule')}.md"
            if target.exists():
                existing = read_text(target).rstrip()
                text = existing + "\n\n## Migrated Legacy Content\n\n" + text
            write_utf8(target, text)
        shutil.rmtree(LEGACY_RULE_DIR)

def write_change_log_notes(imported: list[dict]) -> None:
    CHANGE_DIR.mkdir(parents=True, exist_ok=True)
    if any(CHANGE_DIR.glob("*.md")):
        return

    def note(name: str, title: str, bullets: list[str], refs: list[int]) -> None:
        lines = [
            frontmatter(title, ["paper-revision", "migrated-change-log", "layer/evidence"]),
            f"# {title}",
            "",
            "## Change Points",
            "",
        ]
        lines.extend(f"- {bullet}" for bullet in bullets)
        lines += ["", "## Evidence Memories", ""]
        by_id = {int(r.get("id") or -1): r for r in imported}
        for rid in refs:
            record = by_id.get(rid)
            if record:
                lines.append(f"- [[{Path(record['note_file']).stem}]]")
        write_utf8(CHANGE_DIR / f"{name}.md", "\n".join(lines))

    note(
        "2026-06-01 Abstract writing preference",
        "2026-06-01 Abstract writing preference",
        [
            "The abstract opening should state the relation between the study object, intermetallic compound layer thickness/distribution, and performance or bonding outcomes.",
            "The research problem should be prediction of intermetallic compound layer thickness and distribution.",
            "SPH-FEM should be described briefly as supporting the temperature-field inference, not as a detailed interface-description paragraph.",
            "Interface wave size should appear mainly as a validation result.",
            "Do not write a specific 10 μm threshold in the abstract when discussing layer-thickness influence.",
        ],
        [31, 28, 27, 26, 25],
    )
    note(
        "2026-06-01 Introduction first paragraph references",
        "2026-06-01 Introduction first paragraph references",
        [
            "The first introduction paragraph kept its original content while replacing references with recent SCI-oriented sources.",
            "Preferred reference selection emphasizes recent, high-quality, claim-matched sources.",
            "The edited manuscript was saved as manuscript_intro_p1_q1_refs.docx because the original file was locked.",
        ],
        [34],
    )
    note(
        "2026-06-01 Introduction second paragraph structure",
        "2026-06-01 Introduction second paragraph structure",
        [
            "The second introduction paragraph should not read as a direct two-category list.",
            "The flow should move from experimental characterization, to experimental limitations, to numerical simulation, to SPH-related limitations, and then to the remaining gap.",
            "Experimental limitations should be connected to inability to capture transient collision temperature, local melting, and intermetallic compound formation dynamics.",
        ],
        [34],
    )
    note(
        "Paper memory synchronization convention",
        "Paper memory synchronization convention",
        [
            "All paper-related changes, writing preferences, citation decisions, and revision rationales should be synchronized into the paper memory export path.",
            "The Obsidian vault is the structured knowledge layer; latest memory snapshots remain under source memory snapshots.",
        ],
        [35, 36],
    )


def write_legacy_summary_note(conclusions: list[dict]) -> None:
    title = "Legacy migrated - paper writing principle summary"
    PROCESS_DIR.mkdir(parents=True, exist_ok=True)
    lines = [
        frontmatter(title, ["workflow-governance", "legacy-migrated", "layer/reasoning"]),
        f"# {title}",
        "",
        "## Migration Status",
        "",
        "This note replaces the previous principle-summary entry. It is stored in `35_Workflow_Governance` because it explains knowledge-base maintenance rather than manuscript-writing requirements.",
        "",
        "## Current Generalized Rule Set",
        "",
    ]
    for item in conclusions:
        lines.append(f"- [[{item['title']}]]")
    lines += [
        "",
        "## Migrated Project Change Evidence",
        "",
    ]
    for note in sorted(CHANGE_DIR.glob("*.md")):
        lines.append(f"- [[{note.stem}]]")
    lines += [
        "",
        "## Rule",
        "",
        "Legacy project-specific revisions should not remain as isolated notes. They should be converted into generalized rules, linked back to the concrete change records, and kept testable for later papers.",
        "",
    ]
    write_utf8(PROCESS_DIR / f"{title}.md", "\n".join(lines))


def build_conclusions(records: list[dict]) -> list[dict]:
    specs = [
        {
            "id": "G0",
            "title": "Mentor advice has higher priority in paper-memory reasoning",
            "conclusion": "When paper-writing memories conflict, explicit mentor feedback should be treated as higher-weight evidence than earlier self-authored preferences. The self-thinking process should adopt the mentor rule unless later mentor feedback or a clear user override supersedes it.",
            "predicate": lambda r: source_priority_score(r) >= 100,
            "next_test": "Before applying a writing rule, check whether any cited memory has Source `mentor` or Source Priority `mentor_high`; if so, use it to resolve preference conflicts first.",
            "category": "process_governance",
        },
        {
            "id": "G1",
            "title": "Abstract opening should state object-variable-effect",
            "conclusion": "Across domains, an abstract should start from the study object, the key variable or mechanism, and the affected outcome. A broad background opening is weaker when the central scientific relation can be stated directly.",
            "predicate": lambda r: has(r, "abstract") or has(r, "first sentence") or has(r, "摘要"),
            "next_test": "Check whether the first sentence includes object, variable or mechanism, and outcome.",
            "category": "paper_writing",
        },
        {
            "id": "G2",
            "title": "Method description should serve the research purpose",
            "conclusion": "Method descriptions in abstracts and introductions should be scoped to the research purpose. Implementation details should move to the methods section unless they are part of the core contribution.",
            "predicate": lambda r: has(r, "SPH-FEM") or has(r, "method") or has(r, "interface wave"),
            "next_test": "Compress method sentences to method name, analysis object, and inference target.",
            "category": "paper_writing",
        },
        {
            "id": "G3",
            "title": "Literature review should progress through capability and limitation",
            "conclusion": "A literature review should not be a mechanical category list. It should move from what prior work can do, to what remains missing, to why the next method is needed, and finally to the remaining gap addressed by the paper.",
            "predicate": lambda r: has(r, "introduction") or has(r, "second paragraph") or has(r, "literature"),
            "next_test": "Mark each review sentence as capability, limitation, transition, or remaining gap.",
            "category": "paper_writing",
        },
        {
            "id": "G4",
            "title": "Experiment-simulation gaps should be expressed with variables",
            "conclusion": "For papers combining experiments and simulations, the gap should be stated as a missing bridge between observable experimental variables and simulated variables.",
            "predicate": lambda r: has(r, "experiment") and (has(r, "simulation") or has(r, "SPH")),
            "next_test": "Build a three-column table: simulated variable, experimental variable, claimed correspondence.",
            "category": "paper_writing",
        },
        {
            "id": "G5",
            "title": "Reference upgrades must preserve sentence-level support",
            "conclusion": "Newer or higher-ranked references are only better when they directly support the sentence-level claim. Argument-source fit comes before recency and journal rank.",
            "predicate": lambda r: has(r, "reference") or has(r, "citation") or has(r, "JCR"),
            "next_test": "Record sentence claim, candidate source, support relation, year, journal rank, and replacement reason.",
            "category": "paper_writing",
        },
        {
            "id": "G5a",
            "title": "Numeric and abbreviation subscripts must be upright in formulas and prose",
            "conclusion": "In manuscript formulas and ordinary prose, variable bodies should be italic, but numeric subscripts and subscripts that represent English abbreviations, names, or labels must be upright. This applies to displayed formulas, inline formulas, and textual symbol explanations; DOCX checks should inspect run-level formatting rather than relying on flattened plain text.",
            "predicate": lambda r: (
                has(r, "numeric subscripts")
                or has(r, "abbreviation subscripts")
                or has(r, "subscripts must be upright")
                or has(r, "formula symbols in prose")
                or (has(r, "variables italic") and has(r, "labels upright"))
                or (has(r, "正体") and has(r, "下角标"))
            ),
            "next_test": "For every symbol in formulas and prose, classify each subscript as numeric, abbreviation/label, or variable-like; keep numeric and abbreviation/label subscripts upright and only variable-like indices italic.",
            "category": "paper_writing",
        },
        {
            "id": "G6",
            "title": "Writing knowledge should become reusable process memory",
            "conclusion": "Paper edits should be stored as reusable process memory: problem, action, rationale, applicable context, non-applicable context, evidence, and generalized rule.",
            "predicate": lambda r: has(r, "obsidian") or has(r, "automation") or has(r, "memory") or has(r, "iteration"),
            "next_test": "After each edit, separate the project-specific event from the reusable writing rule.",
            "category": "process_governance",
        },
        {
            "id": "G7",
            "title": "Process governance must not become manuscript requirements",
            "conclusion": "Workflow, memory-management, automation, and knowledge-base maintenance rules must be kept separate from paper-writing requirements. They may guide how the knowledge base grows, but they must not be applied as claims, structure, wording, or evaluation criteria for the manuscript itself.",
            "predicate": lambda r: (
                has(r, "workflow logic")
                or has(r, "process governance")
                or has(r, "knowledge-base maintenance")
                or (has(r, "workflow") and (has(r, "paper requirement") or has(r, "manuscript requirement")))
                or (has(r, "工作流") and (has(r, "论文要求") or has(r, "论文的要求")))
            ),
            "next_test": "Before promoting any rule, label it as paper-writing or process-governance; only paper-writing rules may constrain manuscript wording, structure, or claims.",
            "category": "process_governance",
        },
        {
            "id": "G8",
            "title": "RAG retrieval should be a selective loading layer",
            "conclusion": "RAG retrieval should shortlist relevant knowledge-base notes and reduce context loading. It must not replace full evidence review for final generalization, conflict resolution, or manuscript rule promotion.",
            "predicate": lambda r: has(r, "kb-rag") or (has(r, "rag") and (has(r, "selective") or has(r, "token"))),
            "next_test": "For ordinary writing, use RAG to choose candidate notes first; for final summarization or conflict handling, verify the selected notes against full vault evidence before promotion.",
            "category": "process_governance",
        },
        {
            "id": "G9",
            "title": "Project root must expose mandatory harness entrypoint",
            "conclusion": "The project-local harness can only be enforced reliably when root AGENTS.md contains the mandatory harness rule and root run_paper_iteration.ps1 executes tools/paper_iteration.py with the project root. Archived or subdirectory copies are not sufficient active entrypoints.",
            "predicate": lambda r: (
                has(r, "project root harness")
                or has(r, "root-level `AGENTS.md`")
                or has(r, "root `AGENTS.md`")
                or has(r, "run_paper_iteration.ps1")
                or (has(r, "harness") and has(r, "project root"))
            ),
            "next_test": "Before closing any workflow-maintenance task, verify root AGENTS.md, PROJECT_HARNESS_WORKFLOW.md, and run_paper_iteration.ps1 exist, then run the root harness entrypoint successfully.",
            "category": "process_governance",
        },
        {
            "id": "G10",
            "title": "Before creating scripts retrieve and reuse local scripts",
            "conclusion": "Before creating a new helper script, Codex should use the deployed local RAG method and fast local search to find existing scripts in the project. Reuse a suitable script directly, or make a small scoped modification, when that saves tokens and avoids re-deriving tested logic. Create a new script only when no safe local candidate exists or modification would create higher regression risk.",
            "predicate": lambda r: (
                has(r, "before creating scripts")
                or has(r, "new helper script")
                or has(r, "existing script reuse")
                or has(r, "script-reuse")
                or (has(r, "script") and has(r, "token-savings"))
                or (has(r, "local script") and has(r, "reuse"))
            ),
            "next_test": "Before adding a new script, run local RAG plus rg-based script inventory search, inspect the shortlist, and record whether the task reused, patched, or newly created a script.",
            "category": "process_governance",
        },
        {
            "id": "G11",
            "title": "Manuscript content must be confirmed in chat before Word insertion",
            "conclusion": "For user-requested manuscript-content changes, Codex must first provide the proposed revised content in chat and wait for user confirmation before writing that content into Word. This guards against unwanted DOCX edits while still allowing file inspection, formatting checks, RAG, and knowledge-base maintenance before confirmation.",
            "predicate": lambda r: (
                has(r, "chat first before word")
                or has(r, "chat first before word insertion")
                or has(r, "before Word insertion")
                or has(r, "user confirmation")
                or has(r, "聊天框")
                or (has(r, "Word") and has(r, "confirm"))
                or (has(r, "DOCX") and has(r, "confirmation"))
            ),
            "next_test": "Before writing revised manuscript wording into a DOCX, check whether the user has approved the chat version; if not, provide the proposed content in chat and stop before Word insertion.",
            "category": "process_governance",
        },
    ]
    conclusions: list[dict] = []
    for spec in specs:
        evidence = matching(
            records,
            spec["predicate"],
            include_workflow_governance=spec["category"] != "paper_writing",
        )
        if evidence:
            conclusions.append(
                {
                    "id": spec["id"],
                    "title": spec["title"],
                    "conclusion": spec["conclusion"],
                    "memory_evidence": [mem_ref(record) for record in evidence],
                    "next_test": spec["next_test"],
                    "category": spec["category"],
                }
            )
    return conclusions


def has_user_decision(record: dict, *terms: str) -> bool:
    return source_priority_score(record) >= 120 and has(record, *terms)


def resolve_candidate_evidence(imported: list[dict], evidence_notes: list[str]) -> list[dict]:
    by_key: dict[str, dict] = {}
    for record in imported:
        note_file = str(record.get("note_file") or "")
        title = str(record.get("note_title") or memory_title(record))
        keys = {
            title.lower(),
            Path(note_file).stem.lower(),
            note_file.replace("\\", "/").lower(),
        }
        for key in keys:
            if key:
                by_key[key] = record
    resolved: list[dict] = []
    for raw in evidence_notes:
        key = str(raw or "").strip().replace("\\", "/").lower()
        candidates = [key, Path(key).stem.lower()]
        record = next((by_key[candidate] for candidate in candidates if candidate in by_key), None)
        if record and record not in resolved:
            resolved.append(record)
    return resolved


def load_codex_candidate_conclusions(imported: list[dict]) -> list[dict]:
    if not CANDIDATE_RULES_JSON.exists():
        return []
    try:
        raw = json.loads(CANDIDATE_RULES_JSON.read_text(encoding="utf-8-sig"))
    except Exception:
        return []
    items = raw.get("candidate_rules", raw if isinstance(raw, list) else [])
    if not isinstance(items, list):
        return []
    conclusions: list[dict] = []
    for idx, item in enumerate(items, start=1):
        if not isinstance(item, dict):
            continue
        title = str(item.get("title") or "").strip()
        conclusion = str(item.get("conclusion") or "").strip()
        category = str(item.get("category") or "").strip() or "paper_writing"
        if not title or not conclusion or category not in {"paper_writing", "process_governance"}:
            continue
        evidence_notes = item.get("evidence_notes") or item.get("evidence") or []
        if not isinstance(evidence_notes, list):
            continue
        evidence = resolve_candidate_evidence(imported, [str(note) for note in evidence_notes])
        if not evidence:
            continue
        conclusions.append(
            {
                "id": str(item.get("id") or f"C{idx}"),
                "title": title,
                "conclusion": conclusion,
                "memory_evidence": [mem_ref(record) for record in evidence],
                "next_test": str(item.get("next_test") or "Verify this candidate against its cited evidence before applying it."),
                "category": category,
                "candidate_source": "codex_candidate_rules",
                "candidate_rationale": str(item.get("rationale") or ""),
            }
        )
    return conclusions


def detect_conflicts(records: list[dict]) -> list[dict]:
    conflicts: list[dict] = []
    abstract_resolved = any(
        has_user_decision(record, "abstract", "compromise")
        or has_user_decision(record, "abstract opening", "core research relation")
        for record in records
    )
    wave_resolved = any(
        has_user_decision(record, "dual-mainline")
        or has_user_decision(record, "dual mainline")
        or has_user_decision(record, "interface wave", "intermetallic compound", "mainline")
        for record in records
    )
    abstract_records = [r for r in records if has(r, "abstract") or has(r, "摘要")]
    industry = [
        r for r in abstract_records
        if "industry background" in (r.get("content") or "").lower()
        or "行业/应用背景" in (r.get("content") or "")
    ]
    direct = [
        r for r in abstract_records
        if "start directly" in (r.get("content") or "").lower()
        or "direct first sentence" in (r.get("content") or "").lower()
        or "直接" in (r.get("content") or "")
    ]
    if industry and direct and not abstract_resolved:
        combined = sort_by_source_priority(industry + direct)
        top_priority = source_priority_score(combined[0]) if combined else 0
        lower_priority = any(source_priority_score(record) < top_priority for record in combined)
        conflicts.append(
            {
                "topic": "Abstract first sentence framing",
                "reason": "Earlier memory can be read as favoring industry/application background, while later memory requires direct object-variable-effect framing.",
                "priority_resolution": "Resolved by source priority: mentor-sourced records should override lower-priority self-authored preferences." if top_priority >= 100 and lower_priority else "",
                "records": [mem_ref(r) for r in combined[:8]],
            }
        )

    wave_records = [r for r in records if "interface wave" in (r.get("content") or "").lower()]
    central = [r for r in wave_records if "central problem" in (r.get("content") or "").lower() and "not" not in (r.get("content") or "").lower()]
    validation = [r for r in wave_records if "validation" in (r.get("content") or "").lower() or "not foreground" in (r.get("content") or "").lower()]
    if central and validation and not wave_resolved:
        combined = sort_by_source_priority(central + validation)
        top_priority = source_priority_score(combined[0]) if combined else 0
        lower_priority = any(source_priority_score(record) < top_priority for record in combined)
        conflicts.append(
            {
                "topic": "Role of interface wave in paper framing",
                "reason": "Some memory may frame interface wave as central, while later memory treats it only as validation.",
                "priority_resolution": "Resolved by source priority: mentor-sourced records should override lower-priority self-authored preferences." if top_priority >= 100 and lower_priority else "",
                "records": [mem_ref(r) for r in combined[:8]],
            }
        )
    return conflicts


def load_previous() -> list[dict]:
    if not LATEST_JSON.exists():
        return []
    try:
        return json.loads(LATEST_JSON.read_text(encoding="utf-8-sig")).get("conclusions", [])
    except Exception:
        return []


def compare_conclusions(current: list[dict], previous: list[dict]) -> list[dict]:
    prev = [(p.get("id", ""), p.get("conclusion", "")) for p in previous]
    comparison = []
    for item in current:
        best_id = ""
        best_score = 0.0
        for pid, text in prev:
            score = SequenceMatcher(None, item.get("conclusion", ""), text).ratio()
            if score > best_score:
                best_id, best_score = pid, score
        status = "unchanged" if best_score >= 0.92 else "refined" if best_score >= 0.65 else "new"
        comparison.append(
            {
                "id": item["id"],
                "status": status,
                "closest_previous_id": best_id,
                "similarity": round(best_score, 3),
            }
        )
    return comparison


def note_link(record: dict) -> str:
    file = record.get("file")
    title = record.get("title") or ""
    return Path(file).stem if file else title


def split_conclusions(conclusions: list[dict]) -> tuple[list[dict], list[dict]]:
    paper_rules = [item for item in conclusions if item.get("category") == "paper_writing"]
    process_rules = [item for item in conclusions if item.get("category") != "paper_writing"]
    return paper_rules, process_rules


def is_paper_writing_rule(item: dict) -> bool:
    return item.get("category") == "paper_writing"


def build_final_rule_layers(conclusions: list[dict], conflicts: list[dict]) -> tuple[list[dict], list[dict]]:
    unresolved_conflict_notes = {
        note_link(record)
        for conflict in conflicts
        if not conflict.get("priority_resolution")
        for record in conflict.get("records", [])
    }
    final_rules: list[dict] = []
    limited_rules: list[dict] = []
    for item in conclusions:
        support = item.get("graph_support", {})
        evidence_titles = {note_link(mem) for mem in item.get("memory_evidence", [])}
        related_unresolved = sorted(evidence_titles & unresolved_conflict_notes)
        support_count = support.get("supporting_memory_count", len(item.get("memory_evidence", [])))
        mentor_count = support.get("mentor_evidence_count", 0)
        if not is_paper_writing_rule(item):
            continue
        generalized = not related_unresolved and (support_count >= 2 or mentor_count >= 1)
        payload = {
            "id": item["id"],
            "title": item["title"],
            "conclusion": item["conclusion"],
            "category": item.get("category", "process_governance"),
            "memory_evidence": item.get("memory_evidence", []),
            "next_test": item.get("next_test", ""),
            "supporting_memory_count": support_count,
            "mentor_evidence_count": mentor_count,
            "unresolved_conflict_notes": related_unresolved,
            "generalization_status": "final" if generalized else "limited",
            "graph_support": item.get("graph_support", {}),
        }
        if generalized:
            final_rules.append(payload)
        else:
            limited_rules.append(payload)
    return final_rules, limited_rules


def render_skill_rule_snapshot(final_rules: list[dict]) -> str:
    lines = [
        "## Current Final Writing Rules Snapshot",
        "",
        "This section is auto-generated from `paper_writing_obsidian_vault/40_Final_Generalized_Rules`.",
        "Use these rules directly when the `SCI-memory` skill is invoked for drafting, revision, or analysis.",
        "",
    ]
    for item in final_rules:
        lines += [
            f"### {item['title']}",
            "",
            item["conclusion"],
            "",
        ]
    return "\n".join(lines).rstrip()


def sync_sci_memory_skill(final_rules: list[dict]) -> None:
    if not SCI_MEMORY_SKILL.exists():
        return
    current = read_text(SCI_MEMORY_SKILL)
    generated = f"{SKILL_RULES_START}\n{render_skill_rule_snapshot(final_rules)}\n{SKILL_RULES_END}"
    pattern = re.compile(rf"{re.escape(SKILL_RULES_START)}[\s\S]*?{re.escape(SKILL_RULES_END)}", re.MULTILINE)
    if pattern.search(current):
        updated = pattern.sub(generated, current)
    else:
        updated = current.rstrip() + "\n\n" + generated + "\n"
    if updated != current:
        write_utf8(SCI_MEMORY_SKILL, updated)


def render_conclusion_md(conclusions: list[dict], comparison: list[dict], conflicts: list[dict], imported: list[dict], files: list[EvidenceFile], graph: dict) -> str:
    comp = {item["id"]: item for item in comparison}
    paper_rules, process_rules = split_conclusions(conclusions)
    final_rules, limited_rules = build_final_rule_layers(conclusions, conflicts)
    supervision_priority_notes = load_supervision_priority_notes()
    lines = [
        "---",
        f"title: Iteration {datetime.now().strftime('%Y%m%d_%H%M%S')}",
        f"created: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "tags:",
        "  - layer/output",
        "  - memory-grounded",
        "  - paper-iteration",
        "---",
        "",
        "# Memory-grounded Paper Iteration",
        "",
        "## Scope",
        "",
        "- Paper memories are read from existing notes in `20_Paper_Memories`.",
        "- Every conclusion below cites memory notes.",
        "- Mentor-sourced notes marked `Source: mentor` or `Source Priority: mentor_high` are treated as higher-weight evidence than self-authored preferences.",
        "- Active supervision corrections are treated as the next-highest execution constraints after mentor feedback, scoped by their application area.",
        "- Vault `[[wikilinks]]` and frontmatter tags are parsed into evidence, reasoning, and output graph layers.",
        "- Only the Evidence Graph contributes to support scores; reasoning and output links are audit context only.",
        "- Process-governance conclusions are reported separately and must not be treated as manuscript-writing requirements.",
        "- Current workspace files are scanned as auxiliary evidence.",
        "- No external knowledge is used.",
        "",
        "## Layered Vault Graph Summary",
        "",
        f"- Markdown notes: `{len(graph['nodes'])}`",
        f"- Isolated notes: `{len(graph['orphans'])}`",
        f"- Evidence-layer isolated notes: `{len(graph['evidence_orphans'])}`",
        "- Latest graph analysis: [[graph_analysis_latest]]",
        "",
        "## Current Paper Memory Notes",
        "",
    ]
    for record in imported:
        lines.append(f"- [[{Path(record['note_file']).stem}]]")

    lines += ["", "## Active Supervision Priority Constraints", ""]
    lines += [
        "- These constraints come from `45_Supervision`.",
        "- They are applied below mentor feedback and above ordinary 10/20/30-layer records when their scope matches the task.",
        "- They constrain generation and checking, but workflow/audit rationale must not be inserted into manuscript body text.",
        "",
    ]
    if supervision_priority_notes:
        for note in supervision_priority_notes:
            scope = note.get("scope") or "unspecified"
            lines.append(
                f"- [[{note_link(note)}]] | priority `{note.get('source_priority')}` | scope `{scope}` | score `{source_priority_score(note)}`"
            )
    else:
        lines.append("- No active high-priority supervision constraints detected.")

    lines += ["", "## Final Generalized Paper-Writing Rules", ""]
    lines += [
        "- These final rules are summarized from the current intermediate rules in `30_Writing_Rules`.",
        "- Only `paper_writing` rules with enough evidence support and no unresolved contradiction are promoted into `40_Final_Generalized_Rules`.",
        "- `process_governance` rules are excluded from this section so workflow logic cannot become manuscript requirements.",
        "",
    ]
    for item in final_rules:
        c = comp.get(item["id"], {})
        lines += [
            f"### {item['id']} {item['title']}",
            "",
            f"- Status: `{c.get('status', 'new')}`",
            f"- Closest previous: `{c.get('closest_previous_id', '')}`",
            f"- Similarity: `{c.get('similarity', 0)}`",
            "",
            item["conclusion"],
            "",
            "**Graph Support**",
            "",
            f"- Evidence relation score: `{item.get('graph_support', {}).get('graph_relation_score', 0)}`",
            f"- Mentor-priority evidence notes: `{item.get('graph_support', {}).get('mentor_evidence_count', 0)}`",
            "- Reasoning/output nodes excluded from support score.",
            "",
            "**Memory Evidence**",
            "",
        ]
        for mem in item["memory_evidence"]:
            priority = f" priority `{mem.get('source_priority')}`" if mem.get("source_priority") else ""
            lines.append(f"- [[{note_link(mem)}]]{priority}: {mem.get('content', '')[:240]}")
        lines += ["", "**Next Test**", "", item["next_test"], ""]

    lines += ["## Limited Or Not-Yet-Generalizable Rules", ""]
    if limited_rules:
        lines += [
            "- These rules stay in folder `60_Limited_Rules` for now because the current evidence is still too local or still blocked by unresolved contradiction.",
            "",
        ]
        for item in limited_rules:
            c = comp.get(item["id"], {})
            lines += [
                f"### {item['id']} {item['title']}",
                "",
                f"- Status: `{c.get('status', 'new')}`",
                f"- Closest previous: `{c.get('closest_previous_id', '')}`",
                f"- Similarity: `{c.get('similarity', 0)}`",
                f"- Supporting memory count: `{item.get('supporting_memory_count', 0)}`",
                f"- Mentor-priority evidence notes: `{item.get('mentor_evidence_count', 0)}`",
                "",
                item["conclusion"],
                "",
                "**Limitation**",
                "",
                f"- Unresolved conflict notes: `{', '.join(item.get('unresolved_conflict_notes', [])) or 'none'}`",
                "",
                "**Memory Evidence**",
                "",
            ]
            for mem in item["memory_evidence"]:
                priority = f" priority `{mem.get('source_priority')}`" if mem.get("source_priority") else ""
                lines.append(f"- [[{note_link(mem)}]]{priority}: {mem.get('content', '')[:240]}")
            lines += ["", "**Next Test**", "", item["next_test"], ""]
    else:
        lines.append("- No limited rules this run.")

    lines += ["## Process Governance Rules Not Applied As Paper Requirements", ""]
    if process_rules:
        lines += [
            "- These rules are written to `35_Workflow_Governance`.",
            "- They govern memory, automation, and knowledge-base maintenance only.",
            "- They should not constrain manuscript claims, section structure, wording, or evaluation criteria.",
            "",
        ]
        for item in process_rules:
            c = comp.get(item["id"], {})
            support = item.get("graph_support", {})
            lines += [
                f"### {item['id']} {item['title']}",
                "",
                f"- Status: `{c.get('status', 'new')}`",
                f"- Evidence relation score: `{support.get('graph_relation_score', 0)}`",
                f"- Supporting memory notes: `{support.get('supporting_memory_count', len(item.get('memory_evidence', [])))}`",
                "",
                item["conclusion"],
                "",
                "**Governance Test**",
                "",
                item["next_test"],
                "",
            ]
    else:
        lines.append("- No process-governance rules this run.")

    lines += ["## Intermediate Paper-Writing Rules In 30_Writing_Rules", ""]
    lines += [
        "- This layer is generated from `20_Paper_Memories` and now stores paper-writing rules only.",
        "- Workflow and process-governance rules are stored separately in `35_Workflow_Governance`.",
        "",
    ]
    for item in paper_rules:
        lines.append(f"- [[{item['title']}]] | category `{item.get('category', 'process_governance')}`")

    lines += ["## Conflicts Requiring User Analysis", ""]
    if conflicts:
        for conflict in conflicts:
            lines += [f"### {conflict['topic']}", "", conflict["reason"], ""]
            if conflict.get("priority_resolution"):
                lines += ["**Priority Resolution**", "", conflict["priority_resolution"], ""]
            for record in conflict["records"]:
                lines.append(f"- [[{note_link(record)}]]: {record.get('content', '')[:240]}")
            lines.append("")
    else:
        lines.append("- No unresolved conflicts were detected.")

    lines += ["", "## Workspace Evidence Manifest", ""]
    for item in files:
        lines.append(f"- `{item.path}` | chars `{len(item.text)}` | sha256 `{item.sha256[:12]}`")
    return "\n".join(lines)


def write_rule_notes(conclusions: list[dict]) -> None:
    RULE_DIR.mkdir(parents=True, exist_ok=True)
    for old in RULE_DIR.glob("*.md"):
        old.unlink()
    for item in conclusions:
        if not is_paper_writing_rule(item):
            continue
        title = item["title"]
        rule_type = item.get("category", "process_governance")
        lines = [
            frontmatter(title, ["writing-rule", item["id"], f"rule-type/{rule_type}", "layer/reasoning"]),
            f"# {title}",
            "",
            "## Rule Type",
            "",
            f"- `{rule_type}`",
            "",
            "## Generalized Rule",
            "",
            item["conclusion"],
            "",
            "## Evidence Memories",
            "",
        ]
        for mem in item["memory_evidence"]:
            lines.append(f"- [[{note_link(mem)}]]")
        lines += ["", "## Reuse Test", "", item["next_test"], ""]
        write_utf8(RULE_DIR / f"{sanitize_filename(title, item['id'])}.md", "\n".join(lines))


def write_process_governance_notes(conclusions: list[dict]) -> None:
    PROCESS_DIR.mkdir(parents=True, exist_ok=True)
    for old in PROCESS_DIR.glob("*.md"):
        old.unlink()
    for item in conclusions:
        if is_paper_writing_rule(item):
            continue
        title = item["title"]
        rule_type = item.get("category", "process_governance")
        lines = [
            frontmatter(title, ["workflow-governance", item["id"], f"rule-type/{rule_type}", "layer/reasoning"]),
            f"# {title}",
            "",
            "## Rule Type",
            "",
            f"- `{rule_type}`",
            "",
            "## Governance Rule",
            "",
            item["conclusion"],
            "",
            "## Boundary",
            "",
            "- This rule governs the knowledge-base workflow only.",
            "- It must not be treated as a manuscript claim, section-structure requirement, wording rule, or paper evaluation criterion.",
            "",
            "## Evidence Memories",
            "",
        ]
        for mem in item["memory_evidence"]:
            lines.append(f"- [[{note_link(mem)}]]")
        lines += ["", "## Governance Test", "", item["next_test"], ""]
        write_utf8(PROCESS_DIR / f"{sanitize_filename(title, item['id'])}.md", "\n".join(lines))


def write_final_rules(final_rules: list[dict]) -> None:
    FINAL_RULE_DIR.mkdir(parents=True, exist_ok=True)
    for old in FINAL_RULE_DIR.glob("*.md"):
        old.unlink()
    for item in final_rules:
        title = item["title"]
        lines = [
            frontmatter(title, ["final-generalized-rule", item["id"], f"rule-type/{item.get('category', 'process_governance')}", "layer/reasoning"]),
            f"# {title}",
            "",
            "## Final Generalized Rule",
            "",
            item["conclusion"],
            "",
            "## Derived From Intermediate Rule",
            "",
            f"- [[{title}]]",
            "",
            "## Evidence Basis",
            "",
            f"- Supporting memory count: `{item.get('supporting_memory_count', 0)}`",
            f"- Mentor-priority evidence notes: `{item.get('mentor_evidence_count', 0)}`",
            "",
            "## Evidence Memories",
            "",
        ]
        for mem in item["memory_evidence"]:
            lines.append(f"- [[{note_link(mem)}]]")
        lines += ["", "## Reuse Test", "", item["next_test"], ""]
        write_utf8(FINAL_RULE_DIR / f"{sanitize_filename(title, item['id'])}.md", "\n".join(lines))


def write_conflict_notes(conflicts: list[dict]) -> None:
    CONFLICT_DIR.mkdir(parents=True, exist_ok=True)
    for old in CONFLICT_DIR.glob("*.md"):
        old.unlink()
    if not conflicts:
        write_utf8(
            CONFLICT_DIR / "No unresolved conflicts.md",
            frontmatter("No unresolved conflicts", ["paper-conflict", "layer/reasoning"]) + "# No unresolved conflicts\n",
        )
        return
    for conflict in conflicts:
        title = conflict["topic"]
        lines = [
            frontmatter(title, ["paper-conflict", "layer/reasoning"]),
            f"# {title}",
            "",
            "## Why this needs user analysis",
            "",
            conflict["reason"],
            "",
            "## Conflicting Memories",
            "",
        ]
        for record in conflict["records"]:
            lines.append(f"- [[{note_link(record)}]]: {record.get('content', '')[:260]}")
        if conflict.get("priority_resolution"):
            lines += ["", "## Priority Resolution", "", f"- {conflict['priority_resolution']}", ""]
        else:
            lines += ["", "## User Decision", "", "- Pending.", ""]
        write_utf8(CONFLICT_DIR / f"{sanitize_filename(title, 'conflict')}.md", "\n".join(lines))


def write_hypotheses(conclusions: list[dict]) -> None:
    return


def write_limited_rules(limited_rules: list[dict]) -> None:
    LIMITED_DIR.mkdir(parents=True, exist_ok=True)
    for old in LIMITED_DIR.glob("*.md"):
        old.unlink()
    for item in limited_rules:
        title = f"Limited rule - {item['title']}"
        lines = [
            frontmatter(title, ["limited-rule", item["id"], f"rule-type/{item.get('category', 'process_governance')}", "layer/reasoning"]),
            f"# {title}",
            "",
            "## Current Rule",
            "",
            item["conclusion"],
            "",
            "## Source Rule",
            "",
            f"- [[{item['title']}]]",
            "",
            "## Why Not Final Yet",
            "",
            f"- Supporting memory count: `{item.get('supporting_memory_count', 0)}`",
            f"- Mentor-priority evidence notes: `{item.get('mentor_evidence_count', 0)}`",
            f"- Unresolved conflict notes: `{', '.join(item.get('unresolved_conflict_notes', [])) or 'none'}`",
            "",
            "## Evidence Memories",
            "",
        ]
        for mem in item["memory_evidence"]:
            lines.append(f"- [[{note_link(mem)}]]")
        lines += ["", "## Next Test", "", item["next_test"], ""]
        write_utf8(LIMITED_DIR / f"{sanitize_filename(title, item['id'])}.md", "\n".join(lines))


def write_templates() -> None:
    return


def prune_old_iteration_artifacts() -> None:
    ITER_DIR.mkdir(parents=True, exist_ok=True)
    patterns = ["Iteration *.md", "iteration_*.json"]
    for pattern in patterns:
        for path in ITER_DIR.glob(pattern):
            path.unlink()


def write_iteration_readme() -> None:
    text = """---
title: Paper Iteration Automation
tags:
  - automation
  - layer/output
  - memory-grounded
  - paper-iteration
---

# Paper Iteration Automation

## Manual Start

Use the Codex manual automation named `论文证据迭代思考（手动启动）`.

The automation runs:

```powershell
powershell -ExecutionPolicy Bypass -File .\\run_paper_iteration.ps1
```

## What It Does

1. Reads existing paper memory notes from `20_Paper_Memories`.
2. Parses vault `[[wikilinks]]` and frontmatter tags as a layered local note graph.
3. Maintains frontmatter layer tags: `layer/evidence`, `layer/reasoning`, and `layer/output`.
4. Generates intermediate paper-writing rules in `30_Writing_Rules`.
5. Writes workflow and process-governance rules in `35_Workflow_Governance`.
6. Promotes sufficiently generalized paper-writing rules into `40_Final_Generalized_Rules`.
7. Lists unresolved contradictions in `50_Conflicts`.
8. Preserves still-limited paper-writing rules in `60_Limited_Rules`.
9. Writes the current iteration, graph analysis, and `layered_graph_overview.md` under `70_Iterative_Thinking`.
10. Optionally validates Codex semantic rule candidates from `70_Iterative_Thinking/codex_candidate_rules.json` before writing them into the proper layer.

## Evidence Rule

Every conclusion must cite existing notes in `20_Paper_Memories` and may use current workspace files only as auxiliary evidence. Vault graph links are structural support only; they do not replace note content evidence. Only `20_Paper_Memories` and `10_Project_Change_Log` belong to the Evidence Graph used for scoring. Reasoning and output layers are audit context only. This automation does not import from the local memory database. The process must not use outside knowledge unless the user explicitly asks for it.

## Obsidian Graph Groups

Use these group filters in Obsidian graph view:

- Evidence: `tag:#layer/evidence`
- Reasoning: `tag:#layer/reasoning`
- Output: `tag:#layer/output`

Use this graph search filter to show only layered knowledge-base nodes:

```text
tag:#layer/evidence OR tag:#layer/reasoning OR tag:#layer/output
```

## Expected Report

After a manual run, report back to the user in this order:

1. Final generalized paper-writing rules from `40_Final_Generalized_Rules`.
2. Limited rules currently held in `60_Limited_Rules`.
3. Workflow/process-governance rules from `35_Workflow_Governance`, explicitly marked as not manuscript requirements.
4. Evidence Graph support strength and structurally isolated evidence notes.
5. Contradictions or unresolved conflicts that require user judgment.
6. The next most concrete writing improvement or validation action.
"""
    write_utf8(ITER_DIR / "README.md", text)


def write_manual_prompt(iteration_json: Path) -> None:
    text = f"""---
title: Codex manual analysis prompt latest
tags:
  - automation
  - layer/output
  - paper-iteration
---

# Codex Manual Analysis Prompt

Use the current project directory and existing `20_Paper_Memories` notes only.

- Iteration JSON: `{iteration_json}`
- Latest conclusions: `{LATEST_JSON}`
- Codex candidate rules: `{CANDIDATE_RULES_JSON}`
- Existing paper memory notes: `{MEMORY_DIR}`
- Intermediate writing rules: `{RULE_DIR}`
- Workflow/process-governance rules: `{PROCESS_DIR}`
- Final generalized rules: `{FINAL_RULE_DIR}`
- Supervision corrections: `{SUPERVISION_DIR}`
- Conflicts: `{CONFLICT_DIR}`
- Limited rules: `{LIMITED_DIR}`
- Layered graph overview: `{ITER_DIR / "layered_graph_overview.md"}`
- Obsidian graph groups: `tag:#layer/evidence`, `tag:#layer/reasoning`, `tag:#layer/output`

Tasks:

1. Verify every generalized conclusion against its listed memory evidence.
2. Use `graph_analysis_latest.md` to inspect layered structural support from vault `[[wikilinks]]` and frontmatter tags.
3. Treat mentor-sourced notes (`Source: mentor` or `Source Priority: mentor_high`) as higher-weight evidence than self-authored preferences when conclusions or conflicts disagree.
4. Report the final generalized paper-writing rules from `40_Final_Generalized_Rules` first so the user can review the latest writing constraints.
5. Report workflow/process-governance rules from `35_Workflow_Governance` separately and explicitly mark them as not manuscript requirements.
6. Report the still-limited rules from `60_Limited_Rules` separately from the final generalized rules.
7. Reject or flag any conclusion not supported by memory or current workspace files.
8. List contradictions that cannot be unified after source-priority handling and explicitly ask the user to resolve them.
9. Propose the next concrete writing improvement or validation step after the contradictions section.

Constraint: graph links are structural support only, not evidence by themselves. Only Evidence Graph links may affect support strength. Do not use outside knowledge unless the user explicitly asks for web or literature search.

Candidate rule schema:

```json
{{
  "candidate_rules": [
    {{
      "id": "C1",
      "title": "Short rule title",
      "category": "paper_writing",
      "conclusion": "Generalized rule text.",
      "evidence_notes": ["Exact 20_Paper_Memories note title"],
      "next_test": "Concrete validation test.",
      "rationale": "Why Codex proposed this rule."
    }}
  ]
}}
```
"""
    write_utf8(ITER_DIR / "Codex_manual_analysis_prompt_latest.md", text)


def write_layered_graph_overview(graph: dict) -> None:
    layer_counts = {"evidence": 0, "reasoning": 0, "output": 0}
    for node in graph["nodes"].values():
        layer_counts[node.layer] = layer_counts.get(node.layer, 0) + 1

    text = f"""---
title: Layered graph overview
tags:
  - layer/output
  - paper-iteration
  - vault-graph
---

# Layered Graph Overview

## Layer Flow

```mermaid
flowchart LR
  A["10_Project_Change_Log<br/>project edit evidence"] --> B["20_Paper_Memories<br/>reusable writing evidence"]
  B --> C["30_Writing_Rules<br/>intermediate paper-writing rules"]
  B --> H["35_Workflow_Governance<br/>workflow and process rules"]
  B --> J["45_Supervision<br/>user-triggered supervision corrections"]
  C --> D["40_Final_Generalized_Rules<br/>final paper-writing rules"]
  C --> E["50_Conflicts<br/>priority and contradiction checks"]
  C --> F["60_Limited_Rules<br/>not-yet-generalizable paper rules"]
  D --> G["70_Iterative_Thinking<br/>current conclusions and graph analysis"]
  H --> G
  J --> G
  E --> G
  F --> G
  G --> I["00_Index<br/>entry and navigation"]

  classDef evidence fill:#0f766e,stroke:#115e59,color:#ffffff;
  classDef reasoning fill:#2563eb,stroke:#1d4ed8,color:#ffffff;
  classDef output fill:#d97706,stroke:#b45309,color:#ffffff;
  class A,B evidence;
  class C,D,E,F,H,J reasoning;
  class G,I output;
```

## Layer Counts

- Evidence: `{layer_counts.get("evidence", 0)}` notes
- Reasoning: `{layer_counts.get("reasoning", 0)}` notes
- Output: `{layer_counts.get("output", 0)}` notes

## Obsidian Graph Filters

- All layers: `tag:#layer/evidence OR tag:#layer/reasoning OR tag:#layer/output`
- Evidence only: `tag:#layer/evidence`
- Evidence and reasoning: `tag:#layer/evidence OR tag:#layer/reasoning`
- Hide output layer: `tag:#layer/evidence OR tag:#layer/reasoning`

## Rule

Only the Evidence Graph contributes to conclusion support scores. Reasoning and output layers are shown for navigation and audit.
"""
    write_utf8(ITER_DIR / "layered_graph_overview.md", text)


def write_iteration_outputs(files: list[EvidenceFile], records: list[dict], imported: list[dict], conclusions: list[dict], comparison: list[dict], conflicts: list[dict], graph: dict, layer_tag_updates: int) -> Path:
    ITER_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    paper_rules, process_rules = split_conclusions(conclusions)
    final_rules, limited_rules = build_final_rule_layers(conclusions, conflicts)
    payload = {
        "iteration": stamp,
        "memory_count": len(records),
        "paper_memory_notes": [{"id": r.get("id"), "title": r.get("note_title"), "file": r.get("note_file")} for r in imported],
        "imported_memory_notes": [],
        "report_source": "40_Final_Generalized_Rules",
        "workflow_governance_source": "35_Workflow_Governance",
        "final_generalized_rules": final_rules,
        "limited_rules": limited_rules,
        "paper_writing_conclusions": paper_rules,
        "process_governance_rules": process_rules,
        "conclusions": conclusions,
        "comparison": comparison,
        "conflicts": conflicts,
        "vault_graph": {
            "node_count": len(graph["nodes"]),
            "orphan_count": len(graph["orphans"]),
            "evidence_orphan_count": len(graph["evidence_orphans"]),
            "orphan_notes": graph["orphans"][:40],
            "evidence_orphan_notes": graph["evidence_orphans"][:40],
            "scoring_layer": "evidence",
            "layer_tag_updates": layer_tag_updates,
        },
        "workspace_files": [{"path": str(f.path).replace("\\", "/"), "sha256": f.sha256, "chars": len(f.text)} for f in files],
        "evidence_rule": "Every conclusion must cite existing paper memory notes in 20_Paper_Memories. Workspace files are auxiliary evidence. No outside knowledge is used. This automation does not import memory from the local memory database.",
    }
    json_text = json.dumps(payload, ensure_ascii=False, indent=2, default=str)
    iteration_json = ITER_DIR / f"iteration_{stamp}.json"
    write_utf8(iteration_json, json_text)
    write_utf8(ITER_DIR / "conclusions_latest.json", json_text)
    md = render_conclusion_md(conclusions, comparison, conflicts, imported, files, graph)
    md_path = ITER_DIR / f"Iteration {stamp}.md"
    write_utf8(md_path, md)
    write_utf8(ITER_DIR / "conclusions_latest.md", md)
    write_utf8(ITER_DIR / "graph_analysis_latest.md", render_graph_analysis(graph, conclusions, conflicts, layer_tag_updates))
    write_layered_graph_overview(graph)
    write_manual_prompt(iteration_json)
    write_iteration_readme()
    return md_path


def update_index(imported: list[dict], conclusions: list[dict], conflicts: list[dict]) -> None:
    index = VAULT / "00_Index.md"
    supervision_priority_notes = load_supervision_priority_notes()
    lines = [
        "---",
        "title: Paper writing self-growing knowledge base index",
        f"updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "tags:",
        "  - index",
        "  - layer/output",
        "  - paper-memory",
        "  - self-growing-knowledge-base",
        "---",
        "",
        "# Paper Writing Self-Growing Knowledge Base",
        "",
        "## Project Change Log",
        "",
    ]
    for note in sorted(CHANGE_DIR.glob("*.md")):
        lines.append(f"- [[{note.stem}]]")
    lines += ["", "## Paper Memory Notes", ""]
    for record in imported:
        lines.append(f"- [[{Path(record['note_file']).stem}]]")
    lines += ["", "## Intermediate Paper-Writing Rules", ""]
    for item in conclusions:
        if item.get("category") == "paper_writing":
            lines.append(f"- [[{item['title']}]]")
    lines += ["", "## Workflow / Process Governance Rules", ""]
    for item in conclusions:
        if item.get("category") != "paper_writing":
            lines.append(f"- [[{item['title']}]]")
    for note in sorted(PROCESS_DIR.glob("*.md")):
        if not any(note.stem == item.get("title") for item in conclusions):
            lines.append(f"- [[{note.stem}]]")
    lines += ["", "## Conflicts", ""]
    if conflicts:
        for conflict in conflicts:
            lines.append(f"- [[{conflict['topic']}]]")
    else:
        lines.append("- [[No unresolved conflicts]]")
    lines += ["", "## Final Generalized Paper-Writing Rules", ""]
    for note in sorted(FINAL_RULE_DIR.glob("*.md")):
        lines.append(f"- [[{note.stem}]]")
    lines += ["", "## Supervision Corrections", ""]
    supervision_notes = [
        note
        for note in sorted(SUPERVISION_DIR.glob("*.md"))
        if note.name != "README.md" and not note.name.startswith("TEMPLATE")
    ]
    if supervision_notes:
        for note in supervision_notes:
            lines.append(f"- [[{note.stem}]]")
    else:
        lines.append("- No supervision corrections recorded.")
    lines += ["", "## Active High-Priority Supervision Constraints", ""]
    if supervision_priority_notes:
        for note in supervision_priority_notes:
            lines.append(f"- [[{note_link(note)}]] | scope `{note.get('scope') or 'unspecified'}`")
    else:
        lines.append("- No active high-priority supervision constraints detected.")
    lines += ["", "## Limited Rules", ""]
    for note in sorted(LIMITED_DIR.glob("*.md")):
        lines.append(f"- [[{note.stem}]]")
    lines += ["", "## Iteration", "", "- [[conclusions_latest]]", "- [[graph_analysis_latest]]", "- [[layered_graph_overview]]", ""]
    text = "\n".join(lines)
    write_utf8(index, text)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=str(ROOT))
    args = parser.parse_args()
    root = Path(args.root).resolve()

    imported = load_existing_paper_memory_notes()
    records = imported
    previous = load_previous()
    conclusions = build_conclusions(imported)
    conclusions.extend(load_codex_candidate_conclusions(imported))
    comparison = compare_conclusions(conclusions, previous)
    conflicts = detect_conflicts(imported)
    write_rule_notes(conclusions)
    write_process_governance_notes(conclusions)
    write_change_log_notes(imported)
    write_legacy_summary_note(conclusions)
    files = collect_workspace_evidence(root)
    prune_old_iteration_artifacts()
    layer_tag_updates = ensure_vault_layer_tags()
    graph = collect_vault_graph()
    attach_graph_support(conclusions, conflicts, graph)
    final_rules, limited_rules = build_final_rule_layers(conclusions, conflicts)
    write_final_rules(final_rules)
    write_conflict_notes(conflicts)
    write_limited_rules(limited_rules)
    out = write_iteration_outputs(files, records, imported, conclusions, comparison, conflicts, graph, layer_tag_updates)
    update_index(imported, conclusions, conflicts)
    sync_sci_memory_skill(final_rules)
    print(out)


if __name__ == "__main__":
    main()
