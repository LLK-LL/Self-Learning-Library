---
title: Recurring formula issue fixed by splitting LS-DYNA heat equations
created: 2026-06-04 14:55
tags:
  - docx-formula
  - layer/evidence
  - solution
  - thermal-contact
---

# Problem

The formula-format problem reappeared in the newly inserted LS-DYNA thermal-contact block. The extracted OMML text showed crowded or fragile relations such as combined conductance cases and multiple heat-rate equations in one display line.

# Root Cause

Two issues were identified:

- Complex multi-relation equations were compressed into single display-equation lines, which made Word equation layout fragile.
- Reused lxml/OMML element nodes could move from earlier positions to later positions, causing repeated variables to disappear.

# Fix

The LS-DYNA contact heat-transfer block was rewritten as a sequence of shorter display equations:

- closed-gap conductance
- open-gap conductance
- no-contact conductance
- conductive heat flux
- conductive heat rate
- SPH-side frictional heat rate
- FEM-side frictional heat rate
- SPH-side temperature update
- FEM-side temperature update

# Verification

- Equation numbers are continuous from `(1)` through `(55)`.
- No `#` markers remain.
- No damaged OMML characters, `?`, replacement characters or placeholder boxes were detected in extracted OMML text.
- The standalone `3.4` heading remains absent.
- Present-perfect wording remains absent.
