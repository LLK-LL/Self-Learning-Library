---
title: KB RAG should retrieve selectively and preserve evidence boundaries
tags:
  - kb-rag
  - layer/evidence
  - no-regression
  - paper-memory
  - workflow-governance
---

# KB RAG should retrieve selectively and preserve evidence boundaries

## Problem Pattern

The knowledge base needs lightweight retrieval so ordinary writing tasks do not load every rule and evidence note. However, RAG summaries can become unsafe if they are treated as complete evidence or if workflow-governance notes are retrieved as paper-writing requirements.

## Implementation

The project added `tools/kb_rag.py`, which reuses the local total-agent-memory RAG output style: compact summaries first, then selective full-note loading. It applies project-specific path filtering:

- paper-writing retrieval: `40_Final_Generalized_Rules`, `50_Conflicts`, `60_Limited_Rules`, `30_Writing_Rules`;
- workflow-governance retrieval: `35_Workflow_Governance`;
- optional evidence expansion: `20_Paper_Memories`, `10_Project_Change_Log`.

## Test Result

The latest token-savings test loaded three representative queries. Compared with full loading of the allowed layers, RAG reduced estimated token use from `9119` to `3190`, saving `5929` estimated tokens, or `65.02%`.

## Reusable Rule

RAG should be used as a retrieval and selective-loading layer, not as the final evidence authority. For writing tasks, it should choose candidate rules and conflicts first; for final generalization, conflict resolution, or rule promotion, selected notes must still be checked against the full vault evidence.

## Boundary

- RAG summaries may guide what to open, but they cannot replace full note review when deciding final rules.
- Workflow-governance notes must stay excluded from manuscript-writing rule retrieval unless the task explicitly asks about workflow or knowledge-base maintenance.
- `related_ids` should be retained as optional follow-up links, but not loaded by default when measuring or controlling token usage.
