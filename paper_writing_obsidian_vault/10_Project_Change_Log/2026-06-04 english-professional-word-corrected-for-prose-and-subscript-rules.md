---
title: English professional Word corrected for prose and subscript rules
created: 2026-06-04 23:08
tags:
  - docx-formula
  - layer/evidence
  - professional-formula
---

# English Professional Word Corrected For Prose And Subscript Rules

The user identified five high-priority errors in the English professional Word output:

1. raw subscript notation such as `N_s` remained in prose;
2. formula symbols were replaced by English variable words in prose;
3. explanatory prose contained mathematical symbols and formula fragments;
4. subscript typography needed to be rechecked;
5. calculation operators should be upright, not italic.

Correction applied:

- Rewrote `tools/create_english_professional_reactive_navier_stokes_docx.py` using ASCII source and Unicode escapes for formula symbols.
- Rewrote all prose as natural language without formula symbols, raw subscripts, Greek letters, operators, or equation fragments.
- Moved every mathematical expression into a standalone equation table.
- Simplified notation to avoid unnecessary English-label subscripts: species count is `N`, reaction count is `M`, species source is `S_k`, and heat source is `Q`.
- Generated formulas as professional Word OMML through Word COM BuildUp.

Verification:

- formula tables: `12`
- professional OMML formula objects: `12`
- document tabs: `0`
- number-cell hidden objects: `0`
- bad visible characters and backslash remnants: `0`
- prose tokens `_`, `^`, `=`, Greek symbols, operator symbols, `N_s`, `Q_chem`, `S_k`, `Y_k`, `J_k`: `0`
- professional structures detected: fractions and subscript structures.
