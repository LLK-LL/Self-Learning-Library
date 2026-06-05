---
title: Adjacent formula tables can merge in Word after BuildUp
created: 2026-06-05 00:10
tags:
  - docx
  - formulas
  - layer/evidence
  - no-regression
---

# Memory

During generation of the hyperelastic equation derivation DOCX, Word merged adjacent formula tables when two equation tables appeared with no intervening paragraph. The resulting document had fewer tables than formulas, and equation numbers shifted.

# Application

When using borderless three-column formula tables, do not place two formula tables directly adjacent to each other. Insert a normal explanatory paragraph or another safe separator between formula tables, then verify the final table count and equation numbers after Word BuildUp and save.
