---
title: 2026-06-04 equation numbering and formula-object check
created: 2026-06-04 13:17
tags:
  - docx
  - equation-layout
  - layer/evidence
---

# Change

Created `manuscript_equations_numbered.docx` because `manuscript.docx` was locked by another process and could not be overwritten.

Actions:

- Converted the plain-text formula `vcmax = min(C1, C2)` into a Word OMML equation object.
- Converted embedded source-style equation numbers such as `#8` and `#(19)##` into right-side bracketed numbering.
- Added right-side equation numbers for the inserted thermo-plastic energy equations, numbered `(47)` to `(51)`.
- Applied a Word paragraph layout with a centre tab for the equation and a right tab for the equation number.

# Verification

- No `#` equation-number markers remain in the generated DOCX.
- Formula numbering from `(1)` to `(51)` is complete in the theory section.
- `vcmax = min(C1, C2)` no longer exists as ordinary text.
- The generated DOCX contains Word OMML formula objects.

# File

Generated file: `manuscript_equations_numbered.docx`.

Backup before this operation: `manuscript.before_equation_number_right_align.backup.docx`.
