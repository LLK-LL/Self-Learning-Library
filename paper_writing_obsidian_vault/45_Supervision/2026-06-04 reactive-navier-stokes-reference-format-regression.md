---
title: Reactive Navier-Stokes reference-format regression
created: 2026-06-04 21:58
tags:
  - docx-format
  - docx-formula
  - layer/reasoning
  - supervision
---

# Reactive Navier-Stokes Reference-Format Regression

## User Correction

The user reported that the generated reactive Navier-Stokes Word document repeated previous formatting errors and requested a comparison against the reference article.

## Compared Files

- Reference: `Manuscript-R0319-Without Mark.docx`
- Generated: `Reactive_Navier_Stokes_Derivation_CN.docx`

## Evidence From XML Comparison

Reference article:

- page size: `11906 x 16838` twips (A4)
- margins: top/right/bottom/left `1440 / 1440 / 1440 / 1440`
- footer: `108`
- body paragraphs: `314`
- tables: `5`
- OMML paragraphs: `58`
- OMML objects: `172`
- complex OMML structures include `sSub`, `sSup`, `d`, `f`, `nary`, and other built-up formula nodes.
- most equation-like content appears in paragraphs with OMML formulas and right-side numbers, not as the standalone generated three-column tables used in the failed output.

Generated document:

- page size: `12240 x 15840` twips (Letter)
- margins: top/right/bottom/left `1296 / 1440 / 1296 / 1440`
- footer: `720`
- body paragraphs: `26`
- tables: `12`
- OMML paragraphs: `12`
- OMML objects: `12`
- formula OMML contains only linear `m:t` text inside one run per formula, without built-up complex OMML structure.
- default style remained the `python-docx` default instead of the reference article's document defaults.

## Root Cause

The failure came from substituting local structural checks for reference-format replication:

1. The reference article was not used as the template source before generation.
2. `python-docx` defaults were allowed to create page setup and document defaults, which produced Letter-page geometry and default spacing.
3. The formula check only counted OMML objects and table layout, but did not compare formula-object depth and structure against the reference article.
4. The previous three-column equation-table rule was applied mechanically even though this task explicitly required matching the user's reference article.
5. The no-regression guard verified a narrow local rule set instead of verifying the current task's highest-priority constraint: reference-format consistency.

## Required Future Behavior

For any standalone Word output that the user says should follow the reference article:

- clone page section properties and document defaults from the reference DOCX before inserting content;
- compare generated output against the reference on page size, margins, footer, paragraph defaults, equation placement, and OMML structure;
- do not treat OMML object count as sufficient evidence of correct Word formula formatting;
- if formulas are generated from linear text, either build them up through Word or report that they are linear OMML rather than fully built-up formulas;
- run reference-vs-output XML checks before claiming the format is correct.
