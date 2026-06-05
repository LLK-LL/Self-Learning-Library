---
title: Reactive Navier-Stokes reference-style DOCX regenerated
created: 2026-06-04 22:05
tags:
  - docx-format
  - docx-formula
  - layer/evidence
  - supervision
---

# Reactive Navier-Stokes Reference-Style DOCX Regenerated

The user requested a regenerated Word document to test whether the reference-format regression lesson had been learned.

Generated file:

- `Reactive_Navier_Stokes_Derivation_ReferenceStyle.docx`

Workflow applied:

- Used `Manuscript-R0319-Without Mark.docx` as the DOCX package/template source.
- Replaced only `word/document.xml` body content while preserving reference styles, document defaults, page setup and section properties.
- Used paragraph-based display equations rather than three-column formula tables.
- Added center and right tab stops to equation paragraphs: center `4533`, right `9066`.
- Kept equation numbers on the same line as the formula and aligned via the right tab.

Verification:

- page size matches reference: true
- margins match reference: true
- tables in generated document: `0`
- OMML formula objects: `12`
- equation numbers: `(1)` through `(12)`
- equation paragraphs missing center/right tabs: `0`
- backslash command remnants: `0`
- required key terms present: `Navier-Stokes`, `ω̇_k`, `q̇_chem`, `∂(ρu)/∂t`, `ρc_p`

Implementation note:

- A Word COM BuildUp test was attempted on a command-based formula version, but it left visible backslash commands such as `\partial` and `\mathbf`. That version was rejected and replaced by a Unicode OMML formula version to avoid visible linear-command artifacts.
