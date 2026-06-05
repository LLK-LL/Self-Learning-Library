---
title: Non-Newtonian meta prose and variable italic regression
created: 2026-06-05 00:46
tags:
  - docx
  - formulas
  - layer/reasoning
  - no-regression
  - non-newtonian-fluid
  - supervision
priority: supervision_high
source: user_correction
status: active
scope:
  - theory-formula
  - global-format
---

# Non-Newtonian Meta Prose And Variable Italic Regression

The user found that the non-Newtonian Word output included formatting rationale inside the manuscript body and formatted `eta` and `n` as upright in a viscosity formula where they were variables.

Regression guard:

- manuscript prose must not include formatting rationale, audit logic, rule reminders, or self-check wording;
- symbol explanations should only state symbol meanings;
- `eta` and `n` in non-Newtonian viscosity formulas should remain italic when used as variables;
- numeric subscripts remain upright, but the base variable symbol remains italic;
- run-level checks must distinguish variable bases from numeric subscripts.
