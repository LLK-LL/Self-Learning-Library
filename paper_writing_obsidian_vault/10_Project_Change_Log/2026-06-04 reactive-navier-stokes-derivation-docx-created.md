---
title: Reactive Navier-Stokes derivation DOCX created
created: 2026-06-04 21:30
tags:
  - docx-formula
  - layer/evidence
  - supervision
---

# Reactive Navier-Stokes Derivation DOCX Created

The user entered supervision mode and explicitly requested a new Word document containing a derivation of the Navier-Stokes equations with chemical reaction terms.

The chat-first Word insertion guard was initially followed. The user then clarified that the original command already required direct Word output, so the newer explicit instruction controlled this task.

Generated file:

- `Reactive_Navier_Stokes_Derivation_CN.docx`

Implementation notes:

- Existing local DOCX scripts were inspected first. They targeted `manuscript.docx` editing or chapter extraction and were not safe to reuse directly for this standalone supervision document.
- A scoped generator script was added at `tools/create_reactive_navier_stokes_docx.py`.
- The first PowerShell COM attempt was removed because PowerShell 5 interpreted the Chinese source text with the wrong encoding.
- The final generator uses `python-docx` and inserts display equations as OMML `m:oMathPara/m:oMath` objects.

Verification:

- Output file exists.
- Exact OMML object count: `12`.
- Exact OMML paragraph count: `12`.
- Required terms checked in XML: `Navier-Stokes`, `ω̇_k`, `q̇_chem`, `∂(ρu)/∂t`, and `ρc_p`.
- `tools/check_docx_formula_text.py` produced one conservative warning because it scanned OMML equation text containing `=` as if it were prose; the XML check confirmed the equation was inside OMML rather than ordinary body text.

## Format Regression Correction

The user later reported that the generated Word format was wrong and requested regeneration according to the harness workflow.

Root cause:

- The first standalone version used centered OMML paragraphs, but it did not apply the project-local numbered display-equation table rule.
- It therefore missed the required balanced three-column layout with a pure-text equation-number cell.

Correction:

- `tools/create_reactive_navier_stokes_docx.py` was rebuilt to generate each display equation as a fixed-width borderless three-column table.
- Each equation table now uses grid `1000 / 6306 / 1000`.
- The middle cell contains one centered OMML equation paragraph.
- The right cell contains only visible equation-number text.
- Equation numbers run continuously from `(1)` to `(12)`.

No-regression verification after regeneration:

- equation tables: `12`
- OMML paragraphs: `12`
- number-cell math objects: `0`
- required formula terms remain present.
