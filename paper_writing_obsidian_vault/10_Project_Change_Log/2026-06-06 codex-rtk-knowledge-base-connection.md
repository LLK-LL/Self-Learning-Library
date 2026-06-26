---
title: 2026-06-06 codex-rtk-knowledge-base-connection
created: 2026-06-06
tags:
  - codex
  - knowledge-base-governance
  - layer/evidence
  - rtk
  - workflow
---

# Codex RTK Knowledge-Base Connection

## Change

Created `<codex-home>/RTK.md` so the project root
`AGENTS.md` absolute include resolves successfully for Codex.

## Purpose

The global RTK file now routes Codex into the local project harness when a
workspace exposes `PROJECT_HARNESS_WORKFLOW.md`. In this project, the local
harness remains the primary workflow for writing-rule application,
no-regression checks, paper-memory collection, and rule-layer iteration.

## Verified Scope

- The RTK file is global routing/governance context only.
- It does not add manuscript-writing claims or paper-content requirements.
- The project-local `PROJECT_HARNESS_WORKFLOW.md` remains the controlling
  workflow inside this workspace.

## Evidence

- [[Project harness must be visible from project root]]
- [[KB RAG should retrieve selectively and preserve evidence boundaries]]
- [[Memory destination wording should distinguish total memory from project knowledge base]]

