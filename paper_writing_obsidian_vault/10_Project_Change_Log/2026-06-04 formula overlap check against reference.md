---
title: Formula overlap check against reference
created: 2026-06-04
tags:
  - formula-overlap
  - layer/evidence
  - reference-check
---

# Change

Compared formulas in `manuscript.docx` against formulas in `Manuscript-R0319-Without Mark.docx`.

# Method

- Extracted OMML formula text from both Word documents.
- Normalized whitespace and common dot/punctuation variants.
- Compared each new-paper formula against all reference-paper formulas with sequence similarity.
- Saved detailed reports to `process_files_20260604/formula_overlap_report.json` and `process_files_20260604/formula_overlap_report.md`.

# Result

- New-paper formula count: 59.
- Reference-paper formula count: 172.
- Exact normalized unique overlap: 9 formulas, 15.25% of new-paper unique formulas.
- Near-exact matches at similarity >= 0.95: 17 formulas.
- High matches at 0.85-0.95: 22 formulas.
- Medium matches at 0.70-0.85: 6 formulas.
- Low matches below 0.70: 14 formulas.

# Interpretation

High-overlap formulas mainly occur in the welding-window/Richter formula chain and the SPH/FEM/contact algorithm formulas. The added thermo-plastic energy and heat-contact formulas, including Eqs. (27), (28), (36), (37), and (51)-(59), showed low similarity to the reference formula set.
