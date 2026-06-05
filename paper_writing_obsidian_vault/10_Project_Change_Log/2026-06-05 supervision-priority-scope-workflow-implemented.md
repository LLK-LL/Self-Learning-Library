---
title: Supervision priority scope workflow implemented
created: 2026-06-05 01:25
tags:
  - layer/evidence
  - priority
  - scope
  - supervision
  - workflow
source: user_instruction
status: active
scope:
  - knowledge-base-governance
---

# Supervision Priority Scope Workflow Implemented

## User Requirement

The user approved the recommended model: active supervision corrections should affect Codex thinking and iteration. Their weight should be below explicit mentor feedback, but above ordinary `10`, `20`, and `30` layer records. The user added that high-weight content must distinguish its application scope, such as abstract, introduction, theoretical formulas, global formatting, file reading/processing, and scripts, to prevent manuscript body contamination.

## Implementation

- Updated `PROJECT_HARNESS_WORKFLOW.md` with source-priority and application-scope rules.
- Updated `tools/paper_iteration.py` to parse frontmatter fields beyond tags.
- Updated source-priority scoring so mentor feedback is highest, active supervision corrections are second, and user-confirmed/user-correction records follow.
- Added supervision priority reading from `45_Supervision`.
- Added scope inference and reporting for active supervision constraints.
- Added active supervision constraint sections to iteration reports and `00_Index.md`.
- Added governance memory and workflow-governance notes documenting the new priority model.

## Verification

- `tools/paper_iteration.py` passed Python compilation.
- `run_paper_iteration.ps1` completed successfully.
- The latest iteration report lists active supervision constraints with priority, scope, and score.
- `00_Index.md` lists active high-priority supervision constraints with valid links and scopes.
