---
title: User correction - prose formula symbols require real formatting
created: 2026-06-04 23:08
tags:
  - docx-formula
  - formula-notation
  - layer/evidence
  - user-correction
source: user_correction
priority: user_high
---

# User Correction - Prose Formula Symbols Require Real Formatting

The user corrected several highest-priority formula-writing problems:

- prose should still explain the meaning of symbols used in formulas;
- prose must not contain raw subscript notation such as `N_s`;
- prose must not replace formula symbols such as Greek letters with English placeholder names such as `rho`;
- explanatory prose should use real Word symbols and real subscript or superscript formatting;
- explanatory prose must not contain full mathematical expressions, operator chains, or formula fragments;
- all formulas must be placed as standalone display equations;
- subscript typography must be checked for upright versus italic rules;
- calculation operators such as gradient, divergence, partial derivative and reciprocal operators must be upright, not italic.

## Required Future Behavior

For Word outputs with formulas:

- include symbol explanations in prose when needed;
- write symbols in prose with true Word formatting, not plain-text substitutes;
- replace English placeholder names such as `rho` with the corresponding symbol, such as `ρ`;
- avoid raw underscores and carets in prose;
- put full mathematical expressions and operator chains in standalone equation objects;
- if labels are used as subscripts, keep them upright; variable-like indices may remain italic;
- after professional conversion, check both prose runs and formula objects.

Evidence: user correction during English professional Navier-Stokes generation on 2026-06-04.
