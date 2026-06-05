---
title: Equation layout regression from two-column formula tables
supervision_mode: random_supervision
trigger: old_error_reappeared
correction_type:
  - formula_format_regression
  - rule_misapplied
priority: user_supervision_correction
status: active
tags:
  - docx-formula
  - layer/reasoning
  - supervision
---

# Equation Layout Regression From Two-Column Formula Tables

## User Correction

The user reported on 2026-06-04 that the empty bracket problem still remained and that formulas were again shifted rather than centered.

## Corrected Output

`manuscript.docx` was corrected by rebuilding numbered display-equation tables as balanced three-column tables and by rebuilding number cells as pure text number cells.

## Codex Analysis

- Error type: existing final rule was not applied.
- Root cause: the document still used two-column equation tables with grid widths `7306 / 1000`; this centers the equation within the formula column, not within the full text width.
- Related final rule: `40_Final_Generalized_Rules/Word display equations should use balanced three-column OMML tables.md`.
- Additional defect: final coupled equations were numbered `(62)` and `(63)` instead of `(58)` and `(59)`.

## Evidence Audit

- User correction evidence: the user explicitly stated that empty brackets remained and formula centering regressed.
- Output evidence: XML inspection found two-column equation tables and the `(62)`, `(63)` numbering gap.
- Vault evidence: the final generalized rule already required balanced three-column OMML tables.
- Unsupported inferences removed or marked: no unsupported visual cause was claimed beyond the inspected two-column table structure.

## Required Future Behavior

Before closing any Word formula-format task, verify all numbered display equations use balanced three-column borderless tables, equal-width side cells, centered middle formula cells, and pure text number cells. Do not rely on paragraph centering inside a two-column formula table.

## No-Regression Check

Run an XML check that confirms:

- all numbered equation tables have grid `1000 / 6306 / 1000`;
- each formula row has exactly three cells;
- the number cell has no `m:oMath`, `w:fldChar`, `w:instrText`, or `w:sdt`;
- equation numbers are continuous;
- no empty bracket, `?`, replacement, or placeholder-box character remains.
