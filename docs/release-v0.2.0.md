# v0.2.0 - Updated knowledge vault and portable local RAG

Self-Learning Library v0.2.0 refreshes the public knowledge vault with the latest rule-layer iteration and makes the retrieval scripts easier to run outside the original workstation.

## What is upgraded

- Updated the layered `paper_writing_obsidian_vault` through the 2026-06-26 iteration.
- Added new SCI paper-structure rules for abstract, introduction, theory, numerical simulation, discussion, and conclusion sections.
- Added mentor-derived SCI English translation and grammar rules as focused reusable notes instead of one large source note.
- Added workflow-governance rules for mandatory lightweight RAG startup, RAG repair, script reuse before creating helpers, knowledge-base maintenance ownership, and skill-promotion review.
- Refreshed supervision and no-regression notes for DOCX formula formatting, manuscript-body purity, chat-first Word insertion, and translation checks.
- Added a local fallback retrieval path in `tools/kb_rag.py` so the repository can run without a private `total-agent-memory` checkout.
- Made local paths configurable through environment variables instead of hard-coding one workstation layout.
- Redacted public export artifacts that could expose local absolute paths or full private source text.

## Advantages over v0.1.0

- More complete rule coverage: v0.1.0 mainly demonstrated the harness shape; v0.2.0 includes a richer, iterated knowledge base with 96 change-log notes, 85 paper memories, 15 intermediate writing rules, 12 workflow-governance rules, 15 final generalized rules, and 15 supervision notes.
- Better translation behavior: SCI English grammar rules are now split into targeted retrieval units, making article translation and polishing easier to govern with lightweight RAG.
- Safer publishing posture: raw source-material exports and full-evidence JSON snapshots are omitted from the public release, while derived reusable rules remain available.
- Better portability: the core scripts compile and the lightweight RAG command can run in a fresh clone without private local modules.
- Stronger workflow discipline: the harness now records explicit boundaries for ordinary writing tasks, workflow-governance retrieval, no-regression checks, and script reuse.

## Quick verification

The release was checked with:

```powershell
py -m py_compile tools\kb_rag.py tools\paper_iteration.py
py tools\kb_rag.py --query "SCI English grammar translation article rules" --limit 3
powershell -NoProfile -ExecutionPolicy Bypass -File .\run_paper_iteration.ps1
```

## Current limitations

- The included vault is still a real exported paper-writing workflow, not a synthetic demo vault.
- Some notes mention manuscript filenames as evidence labels, but the manuscript files themselves are not included.
- Convenience commands remain Windows/PowerShell-first.
- The local fallback RAG is intentionally simple; users with a richer memory backend can set `TOTAL_MEMORY_SRC` to reuse their own retrieval implementation.

## Upgrade guidance

Existing users can pull the new release and rerun:

```powershell
py tools\kb_rag.py --query "your task keywords" --limit 3
powershell -NoProfile -ExecutionPolicy Bypass -File .\run_paper_iteration.ps1
```

Optional environment variables:

```powershell
$env:TOTAL_MEMORY_SRC = "C:\path\to\total-agent-memory\src"
$env:TAM_MEMORY_DB = "C:\path\to\memory.db"
$env:SCI_MEMORY_SKILL = "C:\path\to\SCI-memory\SKILL.md"
$env:SELF_LEARNING_LIBRARY_PYTHON = "C:\path\to\python.exe"
```
