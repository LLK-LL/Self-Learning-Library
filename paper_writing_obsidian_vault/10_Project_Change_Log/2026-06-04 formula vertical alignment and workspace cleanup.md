---
title: Formula vertical alignment and workspace cleanup
created: 2026-06-04
tags:
  - docx-formula
  - layer/evidence
  - workspace-cleanup
---

# Change

Corrected remaining formula-layout regressions in `manuscript.docx` and cleaned the project root directory.

# Root Cause

- Some newly written formulas were still linear OMML text rather than stable built-up professional OMML structures.
- Word COM `OMath.BuildUp()` hung on the current document, so batch professional conversion through Word automation was not a reliable path.
- Long fully expanded formulas, especially the FEM energy equation, caused unstable visual stacking.
- Equation table cells needed explicit vertical centering; otherwise the equation number could appear higher than the formula.
- The project root contained non-Word single files, violating the user's required workspace organization.

# Fix

- Compacted the SPH and FEM energy formulas so that complex expressions are not fully expanded in a single display equation.
- Added explicit vertical centering to all formula-table cells.
- Kept all numbered equations in balanced three-column tables.
- Verified equation numbering from `(1)` to `(59)`.
- Moved root-level non-Word single files into `process_files_20260604/`.

# Verification

- `manuscript.docx` is readable.
- All numbered formula tables use `1000 / 6306 / 1000`.
- All formula-table cells have vertical alignment `center`.
- Number cells contain no OMML, field code, or content control.
- No `()`, `?`, replacement character, or placeholder box was found.
- Root directory now contains only folders and `.docx` files.
