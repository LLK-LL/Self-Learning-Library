---
title: LS-DYNA contact heat transfer inserted into SPH-FEM coupling
created: 2026-06-04 14:45
tags:
  - docx-formula
  - layer/evidence
  - sph-fem
  - thermal-contact
---

# Change

The standalone `3.4 Thermo-plastic energy equation for heat calculation` section was removed from `manuscript.docx`.

# Inserted Content

The thermal-contact calculation was inserted into `3.3 SPH-FEM coupling algorithm` after the mechanical SPH-FEM coupling equations. The inserted equations follow the LS-DYNA thermal-contact idea:

- gap-dependent interfacial contact conductance
- conductive heat flux across the FEM-SPH contact interface
- frictional contact work converted into heat and partitioned between the SPH and FEM sides
- SPH-side and FEM-side temperature-update equations with contact heat-source terms

# Verification

- Equation numbers `(1)` through `(51)` remain continuous.
- The old `3.4` heading is no longer present.
- No `#` markers remain.
- No damaged OMML characters or `?` symbols remain in the inserted equations.
- No present-perfect wording remains in extracted prose.
- The backup file was saved under `word_backups/`.
