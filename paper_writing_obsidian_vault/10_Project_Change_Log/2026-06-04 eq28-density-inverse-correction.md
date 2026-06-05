---
title: 2026-06-04 Eq. 28 density inverse correction
created: 2026-06-04
tags:
  - change-log
  - docx
  - formula-correction
  - layer/evidence
---

# Eq. 28 Density Inverse Correction

## Issue

The plastic-work term in Eq. (28) displayed an erroneous density factor resembling `ρ_I^{I-1}`. This is not physically or dimensionally correct for the SPH plastic-work heat-rate expression.

## Correction

The corrected formula is:

`Q̇_I^p = χ m_I ρ_I^{-1} σ_I : ε̇_I^p`

The accompanying explanation was also updated to explain `ρ_I`, `σ_I` and `ε̇_I^p`.

## Output

Because `manuscript.docx` was locked by Word, the corrected version was generated as `manuscript_eq28_fixed.docx`.
