---
title: Energy equation section placement correction
created: 2026-06-04
tags:
  - formulas
  - layer/evidence
  - sph-fem
---

# Change

Corrected the placement and form of the SPH-FEM energy-equation derivation in `manuscript.docx`.

# Details

- Moved the SPH energy equation and SPH heat-conduction contribution into Section 3.1.
- Moved the FEM energy equation and semi-discrete form into Section 3.2.
- Replaced the FEM integral weak-form energy equation with a Gaussian-point summation form consistent with the FEM momentum equation.
- Left only the contact heat-source assembly and final coupled thermal equation in Section 3.3.
- Rebuilt equation-number cells as plain text number cells to remove empty formula placeholders.

# Verification

- `manuscript.docx` was readable through `python-docx`.
- The corrected section text contains separate 3.1, 3.2 and 3.3 energy-equation logic.
- The rewritten formula strings contain no `?` replacement characters in the inspected method-section range.
