---
title: DOCX formula rewrite requires OMML structure check
created: 2026-06-04 12:35
tags:
  - docx
  - formulas
  - layer/evidence
  - no-regression
---

# Memory

When rewriting theoretical formulas from a Word manuscript, plain `python-docx` paragraph text can lose formula structure. In `Manuscript-R0319-Without Mark.docx`, equation objects were stored as OMML math tags; paragraph text flattened roots, fractions, summations, and integral limits.

# Reusable Lesson

Before rewriting or moving formulas into a new manuscript, inspect the DOCX formula object structure, not only the paragraph text. Key formula expressions should be checked against the OMML representation or the rendered Word view before finalizing the rewrite.

# Evidence

Observed during the 2026-06-04 formula rewrite from `Manuscript-R0319-Without Mark.docx` into `manuscript.docx`.
