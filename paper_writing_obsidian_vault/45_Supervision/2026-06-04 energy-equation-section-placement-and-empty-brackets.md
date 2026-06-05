---
title: Energy equation section placement and empty formula brackets
supervision_mode: random_supervision
trigger: old_error_reappeared
correction_type:
  - rule_misapplied
  - formula_format_regression
priority: user_supervision_correction
status: active
tags:
  - formulas
  - layer/reasoning
  - sph-fem
  - supervision
---

# Energy Equation Section Placement And Empty Formula Brackets

## User Correction

The user corrected three problems on 2026-06-04:

- SPH and FEM energy-equation derivations must not be written together in Section 3.3.
- The SPH energy derivation belongs in Section 3.1 and the FEM energy derivation belongs in Section 3.2.
- Some formulas displayed empty bracket or placeholder content in the circled equation-number positions; future formula edits must remove such empty formula-number placeholders.
- The FEM energy equation should follow the same Gaussian summation style as the FEM momentum equation, instead of an integral weak form.

## Corrected Output

`manuscript.docx` was corrected so that:

- SPH energy equations were placed after the SPH momentum equation in Section 3.1.
- FEM energy equations were placed after the FEM momentum equation in Section 3.2.
- Section 3.3 only keeps contact heat source assembly and the final coupled thermal equation.
- Formula number cells were rebuilt as plain text number cells to avoid empty OMML placeholders.

## Codex Analysis

- Error type: rule boundary was incomplete. "Stage by domain" was applied in order, but not placed into the matching 3.1/3.2 subsections.
- Affected rules: `rule-sph-fem-energy-staged-derivation`, DOCX formula placeholder checks.
- Rule override or boundary: when the manuscript already has SPH/FEM method subsections, each domain equation must be placed in the corresponding subsection, not collected near the coupling algorithm.
- Required future behavior: before closing any formula rewrite, inspect both formula math objects and formula-number cells.

## Evidence Audit

- User correction evidence: the current user message explicitly identified section-placement errors, empty bracket placeholders, and the required FEM summation form.
- Output evidence: the previous generated `manuscript.docx` placed SPH and FEM energy equations together near the end of Section 3.3.
- Vault evidence: `30_Writing_Rules/Coupled SPH-FEM energy equations should be staged by domain before assembly.md` required staged SPH/FEM/coupled derivation but did not yet specify subsection placement; this note adds that boundary.
- Unsupported inferences removed or marked: no unsupported cause was added for the empty placeholders; the future requirement is limited to inspecting and removing empty number-cell placeholders.

## Required Future Behavior

For SPH-FEM energy formulas, place SPH derivation in Section 3.1, FEM derivation in Section 3.2, and coupling-only equations in Section 3.3. Use FEM Gaussian summation form when the surrounding FEM method formulas use summation form. Never leave empty brackets or placeholder formula objects in equation-number positions.

## No-Regression Check

Before closing a similar task, check:

- Section 3.1 contains the SPH energy equation if SPH energy is added.
- Section 3.2 contains the FEM energy equation if FEM energy is added.
- Section 3.3 contains only coupling/contact assembly and the final coupled equation.
- Equation number cells contain only visible number text and no empty OMML object.
- No `?`, replacement characters, or empty bracket placeholders remain in formula objects.
