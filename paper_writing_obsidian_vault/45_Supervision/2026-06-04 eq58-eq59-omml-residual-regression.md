---
title: Eq58 Eq59 OMML residual regression
supervision_mode: random_supervision
trigger: old_error_reappeared
correction_type:
  - formula_format_regression
  - rule_misapplied
priority: user_supervision_correction
status: active
tags:
  - docx-formula
  - layer/reasoning
  - supervision
---

# Eq58 Eq59 OMML Residual Regression

## User Correction

The user reported that Eqs. `(58)` and `(59)` repeated the same formula-display error: residual placeholder boxes appeared in the formula area.

## Corrected Output

The formula cells for Eqs. `(58)` and `(59)` in `manuscript.docx` were fully rebuilt instead of only changing text inside the old OMML structure.

## Codex Analysis

- Error type: formula object residual regression.
- Root cause: previous fixes replaced `m:t` text inside existing complex OMML objects, but left old `sSup`, `sSubSup`, delimiter, accent, or other child structures in place. Word rendered those leftover empty structures as placeholder boxes.
- Required boundary: for corrupted Word formulas, do not patch only text nodes inside an existing complex OMML object. Rebuild the formula cell from scratch or use a known-good template.

## Evidence Audit

- User correction evidence: the user supplied a screenshot showing placeholder boxes in Eqs. `(58)` and `(59)`.
- Output evidence: XML inspection found multiple math objects and complex OMML structures inside the affected formula cells before rebuilding.
- Verification evidence: after correction, each affected formula cell contained one `m:oMathPara` and one `m:oMath`, with zero `sSup`, `sSub`, `sSubSup`, delimiter, accent, fraction, radical, limit, field-code, or number-cell math objects.

## Required Future Behavior

When a formula shows placeholder boxes after prior edits, rebuild the entire formula cell. Do not reuse a damaged OMML structure with empty children.

## No-Regression Check

For any formula cell that was previously corrupted, verify:

- exactly one intended math object remains;
- no empty or unintended superscript/subscript/delimiter/accent structures remain;
- the equation-number cell contains no math object;
- no placeholder-box characters or empty brackets are visible in extracted text.
