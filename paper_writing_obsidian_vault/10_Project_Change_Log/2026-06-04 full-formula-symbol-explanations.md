---
title: 2026-06-04 full formula symbol explanations
created: 2026-06-04
tags:
  - change-log
  - docx
  - formula-notation
  - layer/evidence
---

# Full Formula Symbol Explanations

## Change

`manuscript.docx` was revised so formula-neighbouring prose explains newly introduced formula symbols more completely. Existing explanation paragraphs were rebuilt with formatted symbol runs, and missing explanation paragraphs were inserted after formula tables for grouped equations in the theory chapter.

## Scope

- Rebuilt welding-window, Richter, SPH, FEM, contact and coupled thermal-system symbol descriptions.
- Replaced plain-text forms such as `rho`, `beta`, `Delta VJ`, `KB`, `meff`, `CSF` and `KSF` with formatted symbol runs in the explanatory prose.
- Added explanatory paragraphs for formula groups where new symbols were previously not described below the formulas.

## Verification

- Created backup: `word_backups/manuscript_before_full_formula_symbol_explanations_20260604.docx`.
- Ran DOCX extraction around the theory formulas to confirm explanation paragraphs are present.
- Ran run-level inspection for representative symbols, confirming italic base characters and subscript/superscript positions for `K_B`, `m_eff`, `C^{SF}`, `K^{SF}`, `Ṫ^{SF}` and related terms.
