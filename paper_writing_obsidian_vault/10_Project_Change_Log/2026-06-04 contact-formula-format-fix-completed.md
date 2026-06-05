---
title: Contact formula format fix completed
created: 2026-06-04 14:15
tags:
  - docx-formula
  - layer/evidence
  - solution
---

# Fix Completed

The contact-equation region around Eqs. (41)-(44) in `manuscript.docx` was repaired.

# Solution

- Rebuilt damaged OMML display equations for the contact force, penalty stiffness, effective contact mass and traction-balance equations.
- Restored bars, subscripts, superscripts, fractions and the square-root structure.
- Removed stale inline OMML remnants from prose paragraphs so variable strings no longer appear at the paragraph end.
- Replaced present-perfect wording with simple present tense where required.
- Rebuilt Greek/math characters using Unicode code points to avoid Windows PowerShell encoding replacement.

# Verification

- No `#` equation-number markers remained.
- Equation numbers `(1)` through `(51)` were still present.
- No damaged placeholder or replacement characters remained in OMML text.
- No `?` characters remained in OMML text.
- No present-perfect patterns remained in the extracted prose.
- No prose paragraphs retained stray inline OMML formula remnants.
