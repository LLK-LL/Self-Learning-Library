---
title: 2026-06-06 low-token-rag-workflow-rule
created: 2026-06-06
tags:
  - knowledge-base-governance
  - layer/evidence
  - rag
  - token-savings
  - workflow
---

# Low-Token RAG Workflow Rule

## Change

Added the user's workflow rule that knowledge-base retrieval must use RAG and that RAG should be the low-token default path.

## Polished Rule

Knowledge-base retrieval must use the low-token RAG path by default: retrieve compact task-relevant summaries first, load only the matched notes or excerpts needed for the task, and avoid full-vault scanning unless final generalization, conflict resolution, explicit broad review, or verified RAG failure requires it.

## Updated Files

- `PROJECT_HARNESS_WORKFLOW.md`
- `45_Supervision/2026-06-06 mandatory-rag-startup-and-repair.md`
- `35_Workflow_Governance/Mandatory RAG startup and repair before fallback.md`
