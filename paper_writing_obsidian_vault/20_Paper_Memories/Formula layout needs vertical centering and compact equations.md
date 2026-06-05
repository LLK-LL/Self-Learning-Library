---
title: Formula layout needs vertical centering and compact equations
created: 2026-06-04
tags:
  - docx-formula
  - equation-layout
  - layer/evidence
---

# Memory

For Word formula-heavy manuscript edits, centered three-column tables are not enough by themselves. Formula-table cells also need explicit vertical centering, and over-expanded formulas should be compacted into stable display equations.

# Required Future Behavior

- Use balanced three-column formula tables.
- Set vertical alignment to center for every formula-table cell.
- Keep equation-number cells as pure text.
- Avoid fully expanding complex FEM/SPH equations in one display equation.
- Prefer compact assembled expressions plus explanatory text when a fully expanded formula would stack poorly or create unstable Word rendering.
- Do not rely on Word COM batch `OMath.BuildUp()` as the primary repair method because it can hang on complex/malformed formula objects.

# Evidence

- User correction on 2026-06-04 reported that equation numbers were visibly higher than formulas and complex formulas were stacked badly.
- The fix added vertical centering and compacted the FEM energy equation.
- XML verification showed all formula cells have `w:vAlign=center`, all equation numbers are continuous from `(1)` to `(59)`, and no bad placeholder characters remained.
