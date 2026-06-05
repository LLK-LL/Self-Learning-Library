---
title: English professional formula generation debug
created: 2026-06-04 22:48
tags:
  - docx-formula
  - layer/evidence
  - professional-formula
  - supervision
---

# English Professional Formula Generation Debug

The user requested an English Word document with professional Word formulas rather than linear formulas. During the generation attempt, several implementation failures and checks were identified.

Target file attempted:

- `Reactive_Navier_Stokes_Derivation_English_Professional.docx`

## Errors Encountered

1. Direct Word COM `SaveAs` with by-reference PowerShell arguments failed with a type-conversion error.
2. `SaveAs2` to the project path containing Chinese characters timed out.
3. Saving first to an ASCII temporary path on the Desktop and then moving the DOCX into the project folder succeeded.
4. Word COM `OMath.BuildUp()` converted formulas into more professional OMML structures, but the document-level layout check failed.
5. After BuildUp, the generated file contained only `11` formula tables instead of the expected `12`.
6. Equation numbers were `[1,2,3,4,5,6,7,8,9,10,12]`, so `(11)` disappeared.
7. Number-cell `w:noWrap` was missing in all detected formula-number cells.
8. The number-cell hidden-object count was `0`, but no-wrap and numbering continuity still failed.
9. BuildUp simplified or transformed formula text; this means symbol-presence checks must be performed after professional conversion, not before it.
10. A long combined system equation was removed because compact formulas are safer than forcing fully expanded equations into one display line.

## Successful Findings

- A minimal one-formula Word COM test succeeded, proving Word COM can BuildUp and save formulas when the document and path are simple.
- After saving through an ASCII temporary path, the generated professional file had:
  - no visible backslash command remnants;
  - no `?` or replacement characters;
  - professional OMML structures such as `f`, `sSub`, `sSup`, `d`, `num`, and `den`.

## Root Cause

The generation process treated professional formula conversion as if it only affected the formula cell. In practice, Word COM automation and table insertion can alter table/paragraph structure and equation numbering. Therefore, professional conversion must be followed by the full supervision-grade layout audit.

## Required Follow-Up

Before delivering a professional formula DOCX:

- save through an ASCII temporary path if Word COM is used;
- BuildUp formulas one cell at a time;
- after BuildUp, re-check formula-table count, equation-number continuity, number-cell no-wrap, number-cell object contamination, bad characters, visible command remnants and required symbols;
- reject the output if any of these checks fail, even if the formulas look professional.
