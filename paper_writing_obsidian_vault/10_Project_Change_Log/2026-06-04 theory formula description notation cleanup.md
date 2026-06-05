---
title: 2026-06-04 theory formula description notation cleanup
created: 2026-06-04 19:30
tags:
  - docx
  - formula-notation
  - layer/evidence
  - manuscript
---

# 2026-06-04 Theory Formula Description Notation Cleanup

## Trigger

The user reported that formula description text still showed subscript-like strings such as `K_A`/underscore-style notation, and that descriptive prose should not contain operator-like notation such as `SPH-FEM` or slash-style combinations. The user clarified that the modified content was the theory chapter, so the correction scope was narrowed to the theory chapter and previously edited non-theory content was left unchanged.

## Concrete Change

- Updated `manuscript.docx` theory-chapter descriptive text only.
- Replaced prose occurrences of `SPH-FEM` in the theory chapter with wording such as `SPH and FEM` or `coupling scheme for SPH and FEM`.
- Replaced `TC4/Al6061` in the theory chapter with `TC4 and Al6061`.
- Converted underscore or brace notation in prose to real Word subscript/superscript formatting for variables including `h_1`, `h_2`, `v_c`, `C_1`, `C_2`, `H_V`, `K_c`, `Delta V_J`, `N_J`, `K_B`, `A_B`, `V_B`, `m_eff`, `C^{SF}`, `K^{SF}`, and `R^{c,SF}`.
- Checked run-level formatting: variable bodies were italicized; descriptive subscripts/superscripts such as `V`, `max`, `eff`, and `SF` were kept upright.
- Formula bodies, abstract, introduction, and references were not intentionally modified in this cleanup round.

## Verification

- Used `tools/check_docx_formula_text.py` to scan residual operator-like prose and underscore/caret notation.
- Used `tools/inspect_docx_runs.py` to verify run-level italic, subscript, and superscript properties.
- Confirmed the remaining operator-like scan hits in the theory chapter were formula-body lines rather than explanatory prose.

## Workflow Note

This change should have been recorded immediately after the DOCX edit. The record was added after the user pointed out that the knowledge-base/harness step had been missed.
