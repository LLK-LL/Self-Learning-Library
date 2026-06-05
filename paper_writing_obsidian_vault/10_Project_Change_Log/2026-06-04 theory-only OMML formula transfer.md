---
title: 2026-06-04 theory-only OMML formula transfer
created: 2026-06-04 12:46
tags:
  - docx
  - formula-transfer
  - layer/evidence
---

# Change

Updated `manuscript.docx` after user clarification that only the theoretical chapter formulas should be retained.

Actions:

- Removed the previous linear-text formula rewrite block.
- Copied the source DOCX OMML formula objects for `2. Theory of explosion welding` and `3. SPH-FEM algorithm` into `manuscript.docx`.
- Removed non-theory formula material from `4 Numerical simulations`, including JWL, Johnson-Cook, Mie-Gruneisen, and shear-strength formula content.
- Kept the requested SPH-FEM thermo-plastic energy equation as Word equation objects.
- Rebuilt the formula-reference block as `[32]` to `[42]`, matching the theoretical formulas retained in the document.

# Verification

- `4 Numerical simulations`, `4.1.1 Explosive model`, JWL, Johnson-Cook, Mie-Gruneisen, and shear-strength formula text are absent from the target manuscript.
- Target DOCX contains OMML equation tags.
- Theory headings retained: explosion welding window, Richter formula, SPH, FEM, SPH-FEM coupling, and thermo-plastic energy equation.
