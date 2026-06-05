---
title: User correction - reference margins and mixed math run typography
created: 2026-06-04 23:45
tags:
  - correction
  - docx-format
  - formulas
  - layer/evidence
---

# Memory

The user clarified that Word outputs following the reference article must match the reference article margins, not merely use a generic one-inch layout. For the reference article `Manuscript-R0319-Without Mark.docx`, the section properties are page size `11906 x 16838` twips, margins `1440 / 1440 / 1440 / 1440` twips, header `720` twips, footer `108` twips, and gutter `0`.

The user also required a stricter upright/italic check before editing: variables should be italic, variable-like indices may be italic, while numbers, calculation operators, constants, name-like labels, and English abbreviation indices must be upright.

# Application

When Word BuildUp creates OMML formulas, do not assume each math run contains only one typographic category. Mixed runs such as `k=1` must be split or otherwise audited at a finer level so the variable index can remain italic while the equals sign and numeric subscript/limit remain upright.

For formula explanations in body text, use real Word symbol runs and real subscript/superscript formatting. Match the formula typography: variable bodies italic; numeric and label-like subscripts or superscripts upright; identity tensor symbols and change/difference markers upright when they are constants or operators rather than variables.
