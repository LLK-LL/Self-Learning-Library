---
title: Reference-format Word generation must clone and compare reference DOCX
created: 2026-06-04 21:58
tags:
  - docx
  - docx-format
  - layer/evidence
  - no-regression
  - user-preference
source: user_correction
priority: user_high
---

# Reference-Format Word Generation Must Clone And Compare Reference DOCX

When the user asks for a Word document to follow the reference article, generating a fresh `python-docx` document is unsafe unless the reference DOCX's section properties, document defaults, styles, paragraph behavior, and formula placement are cloned or explicitly reproduced.

Before reporting completion, compare the output against the reference DOCX at XML level:

- page size and margins;
- footer/header distances;
- document defaults and key paragraph styles;
- paragraph indentation, alignment, and spacing patterns;
- equation placement method;
- OMML object count and formula-object structure depth, not only the presence of `m:oMath`;
- equation-number placement and whether number text is separate from formula objects.

If the generated formulas are only linear `m:t` text inside OMML, do not present them as matching the reference article's built-up Word formulas.

Evidence: [[2026-06-04 reactive-navier-stokes-reference-format-regression]]
