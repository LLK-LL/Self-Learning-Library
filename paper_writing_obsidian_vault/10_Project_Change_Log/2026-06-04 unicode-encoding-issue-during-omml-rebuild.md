---
title: Unicode encoding issue during OMML formula rebuild
created: 2026-06-04 14:10
tags:
  - docx-formula
  - encoding
  - error-finding
  - layer/evidence
---

# Error

During the OMML rebuild of contact formulas, literal Greek and mathematical symbols passed through a PowerShell here-string were converted into `?` characters in the Word equation XML.

# Root Cause

The script content was transferred through the local Windows console/code-page path, so characters such as kappa, zeta and beta were not preserved safely.

# Fix

The formulas must be rebuilt using explicit Python Unicode code points or escape sequences rather than literal special symbols in the shell-fed script.

# Future Check

OMML no-regression checks must scan for `?`, damaged placeholder boxes and replacement characters in equation text after formula rebuilding.
