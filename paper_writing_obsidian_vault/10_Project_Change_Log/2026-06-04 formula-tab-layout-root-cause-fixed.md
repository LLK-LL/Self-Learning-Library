---
title: Formula tab-layout root cause fixed
created: 2026-06-04 15:05
tags:
  - docx-formula
  - layer/evidence
  - layout
  - root-cause
---

# Problem

Formula lines still showed arrow markers in Word screenshots even after the equation objects and numbering were repaired.

# Root Cause

The arrow markers were Word formatting marks for tab characters. The previous formula layout used center and right tab stops to place the equation and equation number on the same line. When Word's formatting marks were displayed, those tab characters appeared as visible arrows before and after formulas.

The issue was document-wide: all 55 display-equation paragraphs contained tab characters.

# Fix

All display-equation paragraphs were converted from tab-stop paragraphs into borderless two-column tables:

- left cell: centered Word OMML equation object
- right cell: right-aligned equation number

All remaining `<w:tab/>` elements were removed from the document.

# Verification

- Total tab elements in `manuscript.docx`: 0.
- Formula tables: 55.
- Formula tables with tabs: 0.
- Equation numbers `(1)` through `(55)` are continuous.
- No `#` markers remain.
- No damaged OMML characters, `?`, replacement characters or placeholder boxes were detected.
