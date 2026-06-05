---
title: 2026-06-04 numeric and abbreviation subscripts upright rule
created: 2026-06-04 20:50
tags:
  - docx
  - formula-notation
  - layer/evidence
  - user-correction
---

# 2026-06-04 Numeric And Abbreviation Subscripts Upright Rule

## User Instruction

The user clarified a stricter formula-notation rule: subscripts made of numbers and subscripts that represent English word abbreviations must be upright. This requirement applies not only to formula objects, but also to symbols and subscripts appearing in ordinary manuscript text.

## Rule Added

- Numeric subscripts such as `0`, `1`, `2`, and `3` must be upright.
- English-abbreviation or label-like subscripts such as `eff`, `max`, `room`, `melt`, `SF`, `SPH`, and `FEM` must be upright.
- Variable bodies remain italic.
- Genuinely variable-like indices may remain italic.
- DOCX checks must inspect run-level formatting in both formula objects and prose runs, because plain text extraction flattens the typography.

## Knowledge-Base Update

- Updated `20_Paper_Memories/User correction - variables italic constants and labels upright.md`.
- Updated `20_Paper_Memories/Formula symbols in prose must match formula typography.md`.
- Added a new intermediate rule in `30_Writing_Rules`.
