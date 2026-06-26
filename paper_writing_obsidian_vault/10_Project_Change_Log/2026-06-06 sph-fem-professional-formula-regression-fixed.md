---
title: 2026-06-06 sph-fem-professional-formula-regression-fixed
created: 2026-06-06
tags:
  - docx
  - formulas
  - layer/evidence
  - sph-fem
---

# SPH-FEM Professional Formula Regression Fixed

## Change

Fixed the user-reported SPH-FEM formula regression in `manuscript.docx`.

## Problems Found

- The simplified SPH-FEM formulas were not shown as professional Word formulas.
- Prose symbol explanations contained raw underscore notation such as `W_IJ`.
- Formula cells contained residual placeholder/unintended structures.
- Word BuildUp merged adjacent contact-equation tables.
- A Unicode PowerShell path introduced Greek-symbol corruption during an intermediate repair attempt.

## Fix

- Closed the open Word document safely through Word COM.
- Generated clean professional Word formula source content using UTF-8 BOM PowerShell automation.
- Transplanted clean formula cells for Eqs. `(7)`-`(11)` and `(18)`-`(21)`.
- Split the merged contact-equation table back into one equation per table.
- Rebuilt/audited prose symbol formatting and scanned for raw underscore tokens.

## Verification

- target formula cells transplanted: `9`
- merged target tables split: `1`
- bad prose token count: `0`
- target formula table error count: `0`
- retained SPH-FEM coupling schematic remained in place.

## Reusable Lesson

This event is recorded as a supervision correction in `45_Supervision/2026-06-06 SPH-FEM formula professional-format regression.md`.
