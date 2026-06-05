---
title: Formula layout memory scope conflict fixed
created: 2026-06-04 22:18
tags:
  - docx-formula
  - layer/evidence
  - memory-fix
  - supervision
---

# Formula Layout Memory Scope Conflict Fixed

The user corrected the current memory behavior and stated that the afternoon supervision check had been good, while the later outputs repeated earlier formatting errors.

Correction applied:

- The earlier attempted abstraction was corrected after the user pointed out that limiting the good afternoon behavior to supervision mode would allow ordinary tasks to regress.
- The corrected rule is now: the afternoon supervision checks are the minimum quality baseline for all Word formula outputs, not a supervision-only behavior.
- Task classification only adds extra requirements, such as reference DOCX page/style matching; it must not remove the formula-quality baseline.

Resolved rule structure:

- global Word-formula baseline -> formal OMML formula objects, stable equation-number placement, no-wrap equation numbers, no damaged/empty OMML remnants, symbol-presence audit, and visible formula-text audit.
- supervision/formula-learning test -> apply the same baseline with stricter checks from the afternoon supervision output: fixed-layout borderless equation tables, no document tabs, no formula-table tabs, pure-text no-wrap number cells, and fresh OMML nodes for repeated symbols.
- explicit reference-format manuscript request -> add reference DOCX page/style/paragraph matching, but still preserve the global formula baseline.
- existing manuscript formula repair -> inspect existing structure and repair in-place according to accepted manuscript layout, while still preserving the global formula baseline.

Root cause:

- previous memories treated good supervision behavior as task-specific instead of extracting it into a global quality floor;
- retrieval promoted task-specific layout mechanisms to global defaults while failing to preserve the invariant checks;
- the no-regression guard checked the wrong rule family and did not enforce baseline formula correctness in ordinary tasks.
