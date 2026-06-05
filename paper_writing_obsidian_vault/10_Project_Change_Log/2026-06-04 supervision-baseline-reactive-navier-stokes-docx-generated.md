---
title: Supervision-baseline reactive Navier-Stokes DOCX generated
created: 2026-06-04 22:26
tags:
  - docx-formula
  - layer/evidence
  - supervision
---

# Supervision-Baseline Reactive Navier-Stokes DOCX Generated

The user requested another Word generation test after correcting the memory logic. The task was treated as an ordinary Word formula output that must still satisfy the supervision-grade formula baseline.

Generated file:

- `Reactive_Navier_Stokes_Derivation_SupervisionBaseline.docx`

Implementation:

- Added `tools/create_supervision_baseline_reactive_navier_stokes_docx.py`.
- Generated a new file rather than overwriting the earlier failed variants.
- Used fixed-layout borderless three-column formula tables.
- Used one independent OMML formula object per display equation.
- Kept equation-number cells pure text with `w:noWrap`.

Verification:

- formula tables: `12`
- document `w:tab` count: `0`
- formula-table tab count: `0`
- OMML paragraphs: `12`
- OMML formula objects: `12`
- number-cell hidden object count: `0`
- equation numbers: `(1)` through `(12)`
- required symbols present: `ω̇_k`, `q̇_chem`, `∂(ρu)/∂t`, `ρc_p`, `Navier-Stokes`
- visible command-remnant check: no backslash command remnants.

Known checker note:

- `tools/check_docx_formula_text.py` still reports one conservative warning for an equals sign in Eq. (3), because it scans flattened OMML formula text as if it were prose. XML verification confirms the warning is inside a formula object, not ordinary prose.
