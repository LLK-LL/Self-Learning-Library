---
title: Project harness must be visible from project root
created: 2026-06-04 19:37
tags:
  - harness
  - layer/evidence
  - project-root
  - workflow-governance
source: user_correction
priority: user_high
---

# Project Harness Must Be Visible From Project Root

The project-local harness must be enforceable from the workspace root, not only from archived process folders. Future paper-writing or manuscript-editing tasks should rely on root-level files:

- `AGENTS.md` contains the mandatory harness trigger rules.
- `PROJECT_HARNESS_WORKFLOW.md` documents writing-rule application, no-regression guard, and collection workflow.
- `run_paper_iteration.ps1` runs `tools/paper_iteration.py --root <project-root>`.

The root cause of the missed harness run on 2026-06-04 was that the mandatory rule and runnable ps1 entrypoint existed only under `process_files_20260604`, while the active project root exposed only the RTK rule. Subdirectory copies are archival evidence, not active enforcement.

Future guard: before closing workflow-maintenance tasks, verify the three root files exist and run root `run_paper_iteration.ps1` successfully.

Evidence: [[2026-06-04 project-root-harness-enforcement-fixed]]
