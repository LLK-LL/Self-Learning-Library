---
title: English professional Word prose symbol format corrected
created: 2026-06-04 23:16
tags:
  - docx-formula
  - formula-notation
  - layer/evidence
  - professional-formula
---

# English Professional Word Prose Symbol Format Corrected

The user clarified that symbol explanations should remain in prose. The actual requirement was to replace raw text notation with real Word symbols and real subscript formatting, not to remove symbols from explanatory prose.

Correction applied:

- Reintroduced symbol explanations in prose.
- Replaced English placeholders such as `rho`, `mu` and `lambda` with real symbols.
- Used real Word subscript runs for prose symbols such as species mass fraction, diffusion flux, production rate, reaction enthalpy and reaction rate.
- Kept full equations and operator chains in standalone display equations.
- Updated `tools/create_english_professional_reactive_navier_stokes_docx.py`.

Verification:

- raw prose tokens `N_s`, `Q_chem`, `S_k`, `Y_k`, `J_k`: `0`
- English placeholder words `rho`, `mu`, `lambda`: `0`
- prose underscores, carets and equals signs: `0`
- prose subscript runs detected for `k` and `r`
- formula tables: `12`
- professional OMML formula objects: `12`
- document tabs: `0`
- number-cell hidden objects: `0`

Note:

- Flattened DOCX text extraction displays prose symbols such as `Y` with subscript `k` as `Yk`. XML inspection confirmed that the `k` and `r` characters are real Word subscript runs.
