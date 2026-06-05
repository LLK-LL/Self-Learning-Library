---
title: 2026-06-04 Writing retrieval stops at paper memories
tags:
  - kb-rag
  - layer/evidence
  - no-regression
  - workflow-governance
  - writing-retrieval
---

# 2026-06-04 Writing retrieval stops at paper memories

## Change Points

- The user clarified the writing-time retrieval workflow.
- Writing retrieval should proceed by layer from larger/generalized rules to smaller/local rules: `40 -> 50 -> 60 -> 30`.
- If necessary, Codex may follow evidence links from matched `30_Writing_Rules` to `20_Paper_Memories`.
- `20_Paper_Memories` is the lowest writing-time retrieval layer.
- During writing, retrieval must not continue into `10_Project_Change_Log`.

## Evidence Memories

- [[Writing-time retrieval should stop at paper memories]]
