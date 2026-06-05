---
title: SPH-FEM energy equation rewrite
created: 2026-06-04
tags:
  - formulas
  - layer/evidence
  - sph-fem
---

# Change

Rewrote the energy-equation part at the end of Section 3.3 in `manuscript.docx`.

# Details

- Replaced the original two energy update equations, Eqs. (54)-(55), with a staged derivation.
- Added the SPH thermo-plastic energy equation and the SPH conductive heat term as Eqs. (54)-(55).
- Added the FEM weak form and FEM semi-discrete form as Eqs. (56)-(57).
- Added the interface heat-source assembly and final coupled SPH-FEM thermal system as Eqs. (58)-(59).
- Preserved the existing equation-table layout and continued numbering after Eq. (53).
- Created a backup at `word_backups/manuscript_before_energy_equation_rewrite_20260604_1600.docx`.

# Verification

- `manuscript.docx` was readable through `python-docx`.
- Equations (54)-(59) were present once each and in continuous order.
- Each rewritten equation retained an OMML math object.
- No `?` replacement characters were found in the rewritten math text after Unicode repair.
