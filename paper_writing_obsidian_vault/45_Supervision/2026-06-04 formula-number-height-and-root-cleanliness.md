---
title: Formula number height and root directory cleanliness
supervision_mode: random_supervision
trigger: old_error_reappeared
correction_type:
  - formula_format_regression
  - workspace_cleanliness_regression
priority: user_supervision_correction
status: active
tags:
  - docx-formula
  - layer/reasoning
  - supervision
  - workspace-cleanup
---

# Formula Number Height And Root Directory Cleanliness

## User Correction

The user reported on 2026-06-04 that:

- equation numbers were clearly higher than the formulas;
- empty brackets were still a recurring issue;
- all formulas should be professional type;
- overly complex formulas should not be fully expanded and stacked together;
- the project root should contain only folders and Word documents, with other single files moved to a process path.

## Corrected Output

`manuscript.docx` was corrected by compacting the problematic energy equations and adding vertical centering to all formula-table cells. Root-level non-Word files were moved into `process_files_20260604/`.

## Codex Analysis

- Error type: previous no-regression checks verified table width and numbering, but did not verify vertical alignment or root-directory cleanliness.
- Root cause: formula table cells lacked explicit vertical-centering checks, and generated process files were left in the root.
- Additional implementation issue: Word COM `OMath.BuildUp()` hung on the current document, so future fixes must not depend on batch BuildUp as the only route.

## Evidence Audit

- User correction evidence: the user explicitly identified number-height mismatch, complex formula stacking, and root-path clutter.
- Output evidence: before cleanup, the project root contained non-Word files including `.md`, `.json`, `.txt`, and `.ps1`.
- Verification evidence: after correction, XML checks confirmed `w:vAlign=center`, continuous equation numbers `(1)` to `(59)`, and zero bad placeholder characters.
- Unsupported inferences removed or marked: no claim is made that every formula was visually inspected in Word after manual opening; the verified checks are XML-level and readability checks.

## Required Future Behavior

Before closing any Word manuscript formula task:

- verify formula cells and number cells are vertically centered;
- verify number cells are pure text and no empty placeholder remains;
- compact long formulas instead of forcing full expansion into one display equation;
- keep the root directory limited to folders and `.docx` files;
- place process artifacts in a process folder.

## No-Regression Check

Run a final check that reports:

- equation table grid widths;
- vertical alignment status;
- equation-number continuity;
- number-cell object contamination;
- bad placeholder characters;
- root-level non-Word files.
