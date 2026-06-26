---
title: 2026-06-04 project root harness enforcement fixed
created: 2026-06-04 19:33
tags:
  - harness
  - layer/evidence
  - no-regression
  - workflow
---

# 2026-06-04 Project Root Harness Enforcement Fixed

## Failure

During the theory-chapter formula description cleanup, the local harness was not started before the final response. The user asked why the paper knowledge base did not record the change and whether the harness had been started.

## Root Cause

- The mandatory harness instructions existed only under `process_files_20260604/AGENTS.md`, not in the project root.
- The active root-level AGENTS instructions loaded by Codex only referenced `<codex-home>/RTK.md`, so the project-local harness rule was not visible as an active instruction.
- The documented harness entrypoint `run_paper_iteration.ps1` did not exist in the project root.
- The archived `process_files_20260604/run_paper_iteration.ps1` used `$PSScriptRoot\tools\paper_iteration.py`; when run from that subdirectory it incorrectly looked for `process_files_20260604/tools/paper_iteration.py`.

## Fix

- Added root-level `AGENTS.md` containing the RTK rule and mandatory project harness rule.
- Added root-level `PROJECT_HARNESS_WORKFLOW.md` with the enforced writing-rule application, no-regression guard, and collection workflow.
- Added root-level `run_paper_iteration.ps1` that resolves `tools/paper_iteration.py` from the project root and passes `--root`.

## Verification

- `py -m py_compile tools\paper_iteration.py tools\kb_rag.py` passed.
- Root-level `run_paper_iteration.ps1` ran successfully and produced `paper_writing_obsidian_vault/70_Iterative_Thinking/Iteration 20260604_193240.md`.

## Future Guard

For paper-writing or manuscript-changing work in this workspace, future Codex sessions should read root `AGENTS.md`, trigger the local harness, collect records through `10 -> 20 -> 30` when applicable, and run root `run_paper_iteration.ps1` before the final response.
