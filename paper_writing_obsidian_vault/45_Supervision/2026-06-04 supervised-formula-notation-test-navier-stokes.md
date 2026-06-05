---
title: Supervised formula notation test - Navier-Stokes derivation
created: 2026-06-04 15:45
tags:
  - docx-formula
  - layer/reasoning
  - notation
  - supervision
---

# Supervision Trigger

The user entered supervision mode and requested a new Word document containing an English derivation of the Navier-Stokes equations to test whether the learned formula notation and layout rules were applied.

# Checked Rules

- Variables, including tensor, vector and scalar variables, must be italic.
- Constants and name-like symbols must be upright.
- Formula objects must be Word OMML objects.
- Equation layout must use borderless tables, not tabs.
- Equation numbers must be no-wrap and aligned with the body-text right edge.
- English formula descriptions must avoid present perfect tense.

# Error Found During Supervision

The first generated DOCX passed structural layout checks, but several variables disappeared from the extracted formula text. This happened because reused lxml/OMML nodes were moved from earlier formula positions to later positions.

# Correction

The document was regenerated using symbol factory functions so that every variable occurrence received a fresh OMML node. Linear OMML text was then audited in addition to structural checks.

# Verification

For `Navier_Stokes_Derivation.docx`:

- formula count: 10
- missing equation numbers: none
- formula-table tab count: 0
- document tab count: 0
- missing fixed-layout tables: none
- missing no-wrap number cells: none
- damaged OMML characters: 0
- present-perfect patterns: 0
- missing expected formula symbols: none
