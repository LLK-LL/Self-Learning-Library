---
title: Codex RTK include should route into project harness
created: 2026-06-06
tags:
  - codex
  - harness
  - layer/evidence
  - project-root
  - rtk
  - workflow-governance
source: codex_configuration
priority: user_high
---

# Codex RTK Include Should Route Into Project Harness

The project root `AGENTS.md` includes `<codex-home>/RTK.md`.
That global file must exist and must route Codex into the project-local harness
whenever the workspace exposes `PROJECT_HARNESS_WORKFLOW.md`.

For this project, Codex should treat `PROJECT_HARNESS_WORKFLOW.md` as the
primary workflow for writing-rule application, no-regression checks,
paper-memory collection, and rule-layer iteration. The global RTK file is only
a routing and governance layer; it must not replace or weaken the project-local
harness.

Reusable guard: before closing Codex/knowledge-base integration work, verify
that the RTK include resolves, root `AGENTS.md` and `PROJECT_HARNESS_WORKFLOW.md`
exist, RAG retrieval succeeds, and root `run_paper_iteration.ps1` runs
successfully.

Evidence:

- [[2026-06-06 codex-rtk-knowledge-base-connection]]
- [[Project harness must be visible from project root]]
- [[KB RAG should retrieve selectively and preserve evidence boundaries]]
