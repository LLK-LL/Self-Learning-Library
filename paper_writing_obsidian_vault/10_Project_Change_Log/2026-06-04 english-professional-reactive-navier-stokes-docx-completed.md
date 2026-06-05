---
title: English professional reactive Navier-Stokes DOCX completed
created: 2026-06-04 22:55
tags:
  - docx-formula
  - layer/evidence
  - professional-formula
---

# English Professional Reactive Navier-Stokes DOCX Completed

The user asked for the English Word version with professional formulas, not a linear formula version.

Generated file:

- `Reactive_Navier_Stokes_Derivation_English_Professional.docx`

Implementation:

- Used a two-stage workflow:
  1. Python generated stable borderless three-column formula tables.
  2. Word COM opened an ASCII temporary DOCX path and professionalized each formula cell with `OMath.BuildUp()`.
- The final DOCX was moved back into the project folder after Word closed.
- Chemical source notation was stabilized as `S_k` for the species source and `Q_chem` for the reaction heat source to avoid Word's unstable parsing of combining overdot notation.
- Adjacent formula tables were separated by a short prose paragraph because Word merged consecutive tables during professionalization.

Verification:

- formula tables: `12`
- professional OMML formula objects: `12`
- `w:tab` count: `0`
- equation numbers: `(1)` through `(12)`
- number-cell hidden object count: `0`
- visible backslash command remnants: `0`
- bad visible characters `?`, replacement character and placeholder box: `0`
- professional structures detected: `f`, `sSub`, `d`, `num`, and `den`.

Known checker note:

- `tools/check_docx_formula_text.py` reports a conservative warning for Eq. (3) because the flattened OMML formula text contains an equals sign. XML inspection confirms it is inside a formula object.
