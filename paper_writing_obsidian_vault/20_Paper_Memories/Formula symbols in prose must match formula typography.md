---
title: Formula symbols in prose must match formula typography
created: 2026-06-04
tags:
  - docx
  - formula-notation
  - layer/evidence
  - paper-memory
---

# Formula Symbols in Prose Must Match Formula Typography

When formula symbols are explained in the prose below a formula, every newly introduced symbol should be included in the explanation, and the prose symbol must match the formula typography. Variables should remain italic, constants or textual labels used as non-variable indices should stay upright, and subscript/superscript placement should match the corresponding formula.

This requirement is not limited to formulas. When ordinary manuscript prose mentions symbols with subscripts or superscripts, the same typography rules apply. Numeric subscripts must be upright, and subscripts that represent abbreviated English words or name-like labels must also be upright. Examples include `1`, `2`, `0`, `eff`, `max`, `room`, `melt`, `SF`, `SPH`, and `FEM`. Only genuinely variable-like indices should be italic.

For DOCX work, this must be checked at the run level rather than only through plain paragraph text, because plain extraction flattens `K_B`, `m_eff`, `C^{SF}` and similar formatted symbols into ambiguous text.
