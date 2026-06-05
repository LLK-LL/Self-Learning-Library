---
title: Do not patch text inside corrupted OMML formulas
created: 2026-06-04
tags:
  - docx-formula
  - layer/evidence
  - omml
---

# Memory

If a Word formula has already displayed placeholder boxes, replacing only the `m:t` text is unsafe. The old OMML tree may retain empty superscript, subscript, delimiter, accent, fraction, or other structures that Word renders as boxes.

# Required Future Behavior

For corrupted formulas, rebuild the whole formula cell or replace it from a known-good equation template. Then verify the formula cell structure, not just the visible formula string.

# Evidence

Eqs. `(58)` and `(59)` repeated placeholder-box errors after text-node replacement. Rebuilding the affected cells left each formula with one clean math object and no residual complex OMML structures.
