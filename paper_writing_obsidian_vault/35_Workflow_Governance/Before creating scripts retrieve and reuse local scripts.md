---
title: Before creating scripts retrieve and reuse local scripts
created: 2026-06-26 17:13
tags:
  - G10
  - layer/reasoning
  - rule-type/process_governance
  - workflow-governance
---

# Before creating scripts retrieve and reuse local scripts

## Rule Type

- `process_governance`

## Governance Rule

Before creating a new helper script, Codex should use the deployed local RAG method and fast local search to find existing scripts in the project. Reuse a suitable script directly, or make a small scoped modification, when that saves tokens and avoids re-deriving tested logic. Create a new script only when no safe local candidate exists or modification would create higher regression risk.

## Boundary

- This rule governs the knowledge-base workflow only.
- It must not be treated as a manuscript claim, section-structure requirement, wording rule, or paper evaluation criterion.

## Evidence Memories

- [[Before creating scripts retrieve and reuse local scripts]]
- [[KB RAG should retrieve selectively and preserve evidence boundaries]]

## Governance Test

Before adding a new script, run local RAG plus rg-based script inventory search, inspect the shortlist, and record whether the task reused, patched, or newly created a script.
