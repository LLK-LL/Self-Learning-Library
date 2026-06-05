---
title: User correction - equation number parentheses must not wrap
created: 2026-06-04 15:25
tags:
  - correction
  - docx-formula
  - equation-numbering
  - layer/evidence
---

# Memory

The user identified that equation numbers in the formula-table layout wrapped across lines, with the closing parenthesis appearing on a new line. Equation numbers must stay on one line.

# Application

For future DOCX equation layout:

- use a sufficiently wide equation-number cell
- set the table layout to fixed
- set `noWrap` on the equation-number cell
- keep the number paragraph right aligned
- verify that the number cell does not wrap `(n)` into two lines
