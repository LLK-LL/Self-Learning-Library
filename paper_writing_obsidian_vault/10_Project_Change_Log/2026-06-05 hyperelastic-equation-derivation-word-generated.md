---
title: Hyperelastic equation derivation Word generated
created: 2026-06-05 00:10
tags:
  - docx
  - formulas
  - hyperelasticity
  - layer/evidence
  - theory-writing
---

# Hyperelastic Equation Derivation Word Generated

## Task

The user requested a Word document deriving hyperelastic equations according to the project workflow.

## Output

- Generated file: `Hyperelastic_Equation_Derivation_CN_Professional.docx`.
- Generation script: `tools/create_hyperelastic_equations_docx.py`.
- Reused the successful professional formula DOCX workflow from the reactive Navier-Stokes output.

## Content

The document derives hyperelastic equations from motion mapping, deformation gradient, volume change, Cauchy-Green tensors, mass conservation, strain-energy density, Piola stresses, Cauchy stress, and reference/spatial momentum balance. It also gives a compressible Neo-Hookean example.

## Verification

- Reference page setup matched `Manuscript-R0319-Without Mark.docx`: page size `11906 x 16838` twips, margins `1440 / 1440 / 1440 / 1440`, header `720`, footer `108`, gutter `0`.
- Formula tables: `15`.
- OMML formulas: `15`.
- No `w:tab`.
- Formula numbers were no-wrap pure text.
- Professional OMML structures were detected.
- Prose residual check found no raw underscore notation, equality fragments, or English placeholders for Greek symbols.
- Run-level audit confirmed upright markers for operators, digits, transpose labels, and material constants.

## Issue Fixed During Generation

Adjacent formula tables without an intervening paragraph were merged by Word after save, causing equation numbering and table-count regressions. The script was corrected by adding short explanatory paragraphs between consecutive formula tables.
