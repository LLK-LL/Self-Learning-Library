---
title: User preference - equation numbers embedded with right alignment
created: 2026-06-04 13:17
tags:
  - equation-layout
  - layer/evidence
---

# Memory

The user wants each display equation to carry its equation number in the same equation line, with the number placed at the far right of the manuscript page. Source-style markers such as `#8` should be converted into visible bracketed numbers such as `(8)`.

# Application

For future DOCX equation layout work:

- check for formulas still stored as ordinary text
- convert ordinary display formulas into Word OMML equation objects
- remove source markers such as `#8`, `#(19)##`, or dot-leader spacing
- use a centre tab for the formula and a right tab for the equation number
- keep explanatory prose paragraphs separate from display-equation formatting
