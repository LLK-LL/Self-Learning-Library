---
title: Equation layout regression caused by two-column tables
created: 2026-06-04
tags:
  - docx-formula
  - equation-layout
  - layer/evidence
---

# Memory

The recurring formula layout problem in `manuscript.docx` was caused by retaining a two-column equation table layout. Even if the formula paragraph is centered, a two-column layout centers the formula inside only the formula column and can make the whole equation look off center.

# Required Future Behavior

For numbered display equations in this project:

- use a balanced three-column table;
- keep the left spacer cell and right number cell equal width;
- center the OMML formula in the middle cell;
- rebuild the number cell as pure visible text;
- verify that the number cell contains no OMML, field code, content control, placeholder, or empty bracket.

# Evidence

- User correction on 2026-06-04: empty brackets remained and formulas were again visually off center.
- The method-section equation tables were inspected and found to use `7306 / 1000` two-column grids.
- The corrected file uses `1000 / 6306 / 1000` three-column grids and continuous equation numbers from `(1)` to `(59)`.
