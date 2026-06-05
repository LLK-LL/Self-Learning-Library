---
title: Equation number wrapping fixed
created: 2026-06-04 15:25
tags:
  - docx-formula
  - equation-numbering
  - layer/evidence
  - layout
---

# Problem

Equation numbers in the borderless formula tables wrapped across lines, so a number such as `(8)` appeared with the closing parenthesis on the next line.

# Root Cause

The equation-number cell was too narrow and did not include Word `noWrap` protection. The formula tables also lacked fixed table layout, so Word could compress the number cell during layout.

# Fix

All 55 formula tables were updated:

- table width remained aligned to the body text width: 8306 twips
- equation cell width: 7306 twips
- equation-number cell width: 1000 twips
- table layout: fixed
- equation-number cell: `noWrap`
- number paragraph: right aligned and keep-lines enabled

# Verification

- Formula tables: 55.
- All formula table widths: 8306 twips.
- All formula table grids: 7306 + 1000 twips.
- All number cells include `noWrap`.
- Formula tables with tabs: 0.
- Document tab count: 0.
- Equation numbers `(1)` through `(55)` remain continuous.
