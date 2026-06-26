---
title: Project root must expose mandatory harness entrypoint
created: 2026-06-26 17:13
tags:
  - G9
  - layer/reasoning
  - rule-type/process_governance
  - workflow-governance
---

# Project root must expose mandatory harness entrypoint

## Rule Type

- `process_governance`

## Governance Rule

The project-local harness can only be enforced reliably when root AGENTS.md contains the mandatory harness rule and root run_paper_iteration.ps1 executes tools/paper_iteration.py with the project root. Archived or subdirectory copies are not sufficient active entrypoints.

## Boundary

- This rule governs the knowledge-base workflow only.
- It must not be treated as a manuscript claim, section-structure requirement, wording rule, or paper evaluation criterion.

## Evidence Memories

- [[Codex RTK include should route into project harness]]
- [[Project harness must be visible from project root]]

## Governance Test

Before closing any workflow-maintenance task, verify root AGENTS.md, PROJECT_HARNESS_WORKFLOW.md, and run_paper_iteration.ps1 exist, then run the root harness entrypoint successfully.
