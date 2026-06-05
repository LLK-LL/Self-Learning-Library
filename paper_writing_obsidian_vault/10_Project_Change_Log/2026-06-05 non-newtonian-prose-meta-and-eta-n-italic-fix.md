---
title: Non-Newtonian prose meta text and eta n italic fix
created: 2026-06-05 00:46
tags:
  - docx
  - formulas
  - layer/evidence
  - non-newtonian-fluid
  - supervision
---

# Non-Newtonian Prose Meta Text And Eta N Italic Fix

## User Correction

The user identified two problems in `Non_Newtonian_Fluid_Derivation_CN_Professional.docx`:

1. the body text contained process/rule wording such as explaining that a subscript is numeric and should remain upright;
2. in the displayed viscosity formula, `eta` and `n` were variables but had been formatted as upright.

## Fix

- Removed manuscript-body wording that explained formatting rationale.
- Added a visible-prose guard against meta-process terms such as "subscript", "upright", "italic", "should remain", "audit", and "check" in the generated article body.
- Changed formula postprocessing so `eta` and `n` remain italic variables.
- Kept digits and operators upright.

## Verification

- Body prose contained no meta-process wording and no raw formula notation.
- The affected formulas showed `eta` and `n` without upright markers.
- Digits, equation signs and minus signs retained upright markers.
- The DOCX retained `15` formula tables, `15` OMML objects, no tabs, reference page setup, and no-wrap pure-text equation numbers.
