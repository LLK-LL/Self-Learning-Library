---
title: Professional Word formulas require post-BuildUp layout audit
created: 2026-06-04 22:48
tags:
  - docx-formula
  - layer/evidence
  - no-regression
  - professional-formula
source: user_correction
priority: user_high
---

# Professional Word Formulas Require Post-BuildUp Layout Audit

When Word formulas are converted from linear input into professional Word equations, the output must be audited after conversion. It is not enough to verify the pre-conversion linear formula text.

During the English reactive Navier-Stokes generation attempt, Word COM `OMath.BuildUp()` successfully produced professional OMML structures, but the final DOCX still failed layout checks: one equation table disappeared or merged, equation number `(11)` was missing, and number-cell `w:noWrap` was absent.

## Required Future Behavior

For professional Word formula output:

- generate formulas as Word OMML objects;
- run professional conversion only when the formula inputs and document structure are stable;
- prefer compact equations over long combined systems;
- after professional conversion, inspect the final DOCX XML rather than trusting the Word automation call;
- verify formula count, equation-number continuity, number-cell no-wrap, number-cell object contamination, vertical alignment, bad characters, visible command remnants and required symbols;
- do not deliver a professional-formula DOCX if any layout or numbering check fails.

## Implementation Notes

- Word COM may fail or time out when saving directly to a path containing Chinese characters; saving to an ASCII temporary path and moving the final DOCX back to the project folder is safer.
- A minimal one-formula BuildUp test can pass while the full multi-equation document still fails, so the full generated file must always be checked.

Evidence: [[2026-06-04 english-professional-formula-generation-debug]]
