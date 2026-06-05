---
title: 2026-06-04 KB RAG retrieval adapter and token savings test
tags:
  - kb-rag
  - layer/evidence
  - token-savings
  - workflow-governance
---

# 2026-06-04 KB RAG retrieval adapter and token savings test

## Change Points

- Added `tools/kb_rag.py` as a project-local RAG adapter for the Obsidian paper-writing knowledge base.
- The adapter follows compact shortlist -> path/type filtering -> selective full-note loading.
- Paper-writing queries search `40_Final_Generalized_Rules`, `50_Conflicts`, `60_Limited_Rules`, and `30_Writing_Rules`.
- Workflow/governance queries are routed to `35_Workflow_Governance`.
- `35_Workflow_Governance` remains excluded from manuscript-writing retrieval unless the query is about workflow, automation, memory, or knowledge-base maintenance.
- Token savings were tested with three representative queries and recorded in `70_Iterative_Thinking/kb_rag_token_savings_latest.md`.

## Evidence Memories

- [[KB RAG should retrieve selectively and preserve evidence boundaries]]
