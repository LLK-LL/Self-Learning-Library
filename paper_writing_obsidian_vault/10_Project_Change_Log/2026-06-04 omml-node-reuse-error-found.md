---
title: OMML node reuse error found during LS-DYNA heat-transfer insertion
created: 2026-06-04 14:35
tags:
  - docx-formula
  - error-finding
  - layer/evidence
  - xml
---

# Error

During insertion of the LS-DYNA thermal-contact equations, repeated formula symbols disappeared from Eqs. (47)-(49).

# Root Cause

The same lxml element object was reused in multiple positions in an OMML equation. lxml moves an element to its latest parent, so the earlier occurrence is removed from the formula.

# Fix

Repeated mathematical symbols must be rebuilt as fresh OMML nodes each time they appear. Factory functions should be used instead of storing reusable XML element instances.

# Future Check

After generating OMML formulas, inspect the extracted OMML text and verify that repeated variables still appear in every intended position.
