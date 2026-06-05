---
title: Navier-Stokes formula centering corrected
created: 2026-06-04 15:55
tags:
  - docx-formula
  - layer/evidence
  - layout
  - supervision
---

# Problem

The formulas in `Navier_Stokes_Derivation.docx` appeared left-shifted compared with the reference article.

# Root Cause

The formula layout used a two-column borderless table. The left cell contained the centred formula and the right cell contained the equation number. Because the right number cell consumed part of the body-text width, the formula was centred within the remaining left cell rather than within the full body-text area.

# Fix

The formula layout was converted to a balanced three-column table:

- left spacer cell: 1000 twips
- centred formula cell: 6306 twips
- right equation-number cell: 1000 twips
- total table width: 8306 twips

This keeps the formula centred within the body-text width while preserving right-aligned equation numbers.

# Output

Because `Navier_Stokes_Derivation.docx` was open in Word and locked, the corrected file was saved as:

`Navier_Stokes_Derivation_centered.docx`

# Verification

- formula count: 10
- formula table grid: 1000 + 6306 + 1000 twips
- no tab elements
- no wrapped equation numbers
- no damaged OMML characters
