---
title: Writing-time retrieval should stop at paper memories
tags:
  - kb-rag
  - layer/evidence
  - no-regression
  - paper-memory
  - writing-retrieval
---

# Writing-time retrieval should stop at paper memories

## User Instruction

During manuscript writing, retrieval should proceed by layer from general to local: `40_Final_Generalized_Rules -> 50_Conflicts -> 60_Limited_Rules -> 30_Writing_Rules`. If needed, Codex may follow the evidence links in matched `30_Writing_Rules` to `20_Paper_Memories`.

## Reusable Rule

Writing-time retrieval must use the lightweight RAG flow: RAG retrieves relevant rules, Codex turns them into a writing checklist, Codex writes or revises the manuscript, and Codex then runs the no-regression check.

## Boundary

- `20_Paper_Memories` is the lowest writing-time retrieval layer.
- Do not continue from `20_Paper_Memories` into `10_Project_Change_Log` during writing.
- `10_Project_Change_Log` remains useful for collection, audit, and final iteration, but not for ordinary writing retrieval.
