---
title: Three-column equation layout correction
created: 2026-06-04
tags:
  - docx-formula
  - equation-layout
  - layer/evidence
---

# Change

Corrected the equation layout in `manuscript.docx` after the user reported that empty brackets remained and formulas were visually off center.

# Root Cause

- The formula tables still used the old two-column layout: formula cell plus equation-number cell.
- In a two-column layout, the formula is centered only inside the formula cell rather than in the full text-width area, so the displayed equation can appear horizontally shifted.
- Equation-number cells were not rebuilt using the required balanced three-column rule, which left the task vulnerable to visible empty bracket or placeholder artifacts.
- The final coupled equations had been incorrectly numbered as `(62)` and `(63)`, leaving a gap after `(57)`.

# Fix

- Converted numbered display-equation tables to balanced three-column tables: left spacer `1000`, centered formula cell `6306`, right number cell `1000`.
- Rebuilt equation-number cells as pure text cells with no OMML object.
- Corrected the final coupled equations to `(58)` and `(59)`.
- Repaired the symbol text in Eqs. `(58)` and `(59)`.

# Verification

- `manuscript.docx` opened successfully through `python-docx`.
- All equation tables use the `1000 / 6306 / 1000` grid.
- Equation numbers are continuous from `(1)` to `(59)`.
- No duplicate equation numbers were found.
- Number cells contain no OMML math object.
- No `()`, `?`, replacement character, or placeholder box character was found in the inspected formula text.
