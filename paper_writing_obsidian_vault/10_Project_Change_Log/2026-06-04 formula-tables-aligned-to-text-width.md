---
title: Formula tables aligned to text width
created: 2026-06-04 15:15
tags:
  - docx-formula
  - layer/evidence
  - layout
---

# Change

The borderless formula tables in `manuscript.docx` were too wide and placed equation numbers near the page edge rather than the body-text right edge.

# Fix

All 55 formula tables were resized to the body text width:

- page width: 11906 twips
- left margin: 1800 twips
- right margin: 1800 twips
- body text width: 8306 twips
- equation cell width: 7606 twips
- equation-number cell width: 700 twips

# Verification

- Formula tables: 55.
- All formula table widths: 8306 twips.
- All formula table grid widths: 7606 + 700 twips.
- Formula tables with tabs: 0.
- Document tab count: 0.
- Equation numbers `(1)` through `(55)` remain continuous.
