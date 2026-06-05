---
title: English professional Word reference margin and upright italic fix
created: 2026-06-04 23:45
tags:
  - docx
  - docx-format
  - formulas
  - layer/evidence
---

# English Professional Word Reference Margin And Upright Italic Fix

## Trigger

The user corrected two remaining problems in the English reactive Navier-Stokes Word output:

1. the body left and right margins did not match the reference article;
2. upright and italic formatting in both body text and formulas still needed rechecking before further operation.

## Changes

- Reused and patched `tools/create_english_professional_reactive_navier_stokes_docx.py`.
- Locked the generated DOCX section XML to the reference article page setup:
  - page size `11906 x 16838` twips;
  - margins `1440 / 1440 / 1440 / 1440` twips;
  - header `720` twips;
  - footer `108` twips;
  - gutter `0`.
- Set body first-line indent to `239` twips.
- Aligned the three-column formula table width to the reference text width, `9026` twips.
- Added post-BuildUp OMML processing to split mixed math runs such as `k=1` so variable characters can remain italic while equals signs and digits are upright.
- Treated `I` as upright in the identity tensor context and `Delta` as an upright change marker while retaining variable bodies such as `H`, `R`, `Y`, `J`, and `S` as italic.

## Verification

- The generated DOCX and reference article had identical `pgSz` and `pgMar` XML values.
- The generated DOCX contained `12` tables, `12` OMML objects, no `w:tab`, professional fraction and subscript structures, and pure no-wrap equation-number cells.
- Prose residual checks found no raw subscript tokens, English Greek placeholders, formula fragments, or raw operator notation.
- Formula OMML run inspection confirmed that operators, equals signs, digits, transpose `T`, and identity tensor `I` were marked upright while variable letters were left italic.
