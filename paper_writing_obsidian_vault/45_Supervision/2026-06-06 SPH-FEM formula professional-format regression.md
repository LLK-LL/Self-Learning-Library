---
title: SPH-FEM formula professional-format regression
supervision_mode: user_correction
trigger: old_error_reappeared
correction_type:
  - formula_format_regression
  - prose_symbol_regression
  - rule_misapplied
priority: user_supervision_correction
status: active
tags:
  - docx-formula
  - layer/reasoning
  - sph-fem
  - supervision
---

# SPH-FEM Formula Professional-Format Regression

## User Correction

On 2026-06-06, the user reported three repeated errors after the SPH-FEM theory simplification was written back into `manuscript.docx`:

- display formulas were not professional Word formulas;
- prose symbols again used raw underscore notation such as `W_IJ`;
- formula cells showed residual placeholder boxes or unintended content, visible in the SPH approximation formula screenshot.

The user explicitly required this to be fixed and recorded in the project knowledge base so it does not recur.

## Corrected Output

The affected SPH-FEM formulas in `manuscript.docx` were rebuilt from a clean Word professional formula source and transplanted back into the manuscript. The affected formula cells were Eqs. `(7)`-`(11)` and `(18)`-`(21)`.

The correction also split the Word-merged contact formula table back into separate equation tables and preserved the retained SPH-FEM coupling schematic.

## Codex Analysis

- Error type: old DOCX formula-format regression.
- Root cause 1: formulas were created by patching text inside existing OMML/table structures rather than rebuilding from a known-good professional formula source.
- Root cause 2: a PowerShell script containing Unicode formula text was read by Windows PowerShell without a UTF-8 BOM, causing Greek-symbol corruption in Word.
- Root cause 3: Word `OMath.BuildUp()` can merge adjacent equation tables, so adjacent formula tables must be separated and audited after BuildUp.
- Root cause 4: the prose symbol rewrite was not audited at run level; visible plain text can hide the fact that symbols are not real Word subscript/superscript formatting.

## Required Future Behavior

For any DOCX formula edit in this project, especially SPH-FEM theory formulas:

1. Do not patch only `m:t` text inside an existing complex OMML formula when the formula has been edited or corrupted.
2. Rebuild the whole formula cell from a clean known-good professional Word formula source, or generate a clean source DOCX and transplant the formula cell.
3. If Word COM/PowerShell is used with Unicode formulas, write the temporary `.ps1` file with UTF-8 BOM or avoid script-embedded Unicode.
4. After Word `OMath.BuildUp()`, audit for table merging, equation-number continuity, number-cell contamination, placeholder boxes, replacement characters, and malformed/duplicate formula text.
5. Prose formula symbols must use real Word formatting. Raw tokens such as `W_IJ`, `m_J`, `rho_J`, `sigma_I`, `g_dot`, `T_dot`, and `epsilon_dot` are regressions.
6. Adjacent display-equation tables must not be left unchecked after BuildUp; split merged multi-row equation tables back into one equation per table when necessary.

## No-Regression Check

Before closing future DOCX formula tasks, verify:

- all edited display formulas are professional Word OMML formulas, not linear-only text;
- each target formula cell has the intended math object and no residual placeholder structures;
- number cells contain pure text and no math object;
- no raw underscore notation remains in prose symbol explanations;
- no `?`, replacement characters, placeholder boxes, or garbled Greek symbols remain;
- equation tables did not merge after BuildUp.
