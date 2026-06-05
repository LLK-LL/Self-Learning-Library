---
title: 2026-06-04 Abstract opening needs industry and problem background
created: 2026-06-04 12:13
tags:
  - abstract
  - active
  - active-supervision
  - layer/reasoning
  - opening
  - supervision
---

# 2026-06-04 Abstract opening needs industry and problem background

## supervision_mode

active_supervision

## trigger

explicit_supervision_system

## correction_type

missing_industry_background_in_abstract_opening

## priority

user_supervision_correction

## status

active

## user_correction

The user accepted the overall abstract architecture but corrected the opening requirement: the first sentence should briefly state the industry/application background in addition to the problem background. The user gave the example: "超结构已被广泛应用于航空航天的防护中", followed by the problem background.

## codex_analysis

The generated abstract opened directly with the mechanical problem of impact response, deformation mode, stress-wave propagation, and energy dissipation. It did not first state the industry/application background. This is a missing opening-context issue, not an architecture failure.

For future abstract writing in this supervision mode, the first sentence should combine:

1. industry/application background;
2. problem background;
3. the core research relation, when space permits.

This correction is consistent with the existing final rule that an abstract opening may begin from application context but must quickly connect that context to the paper's core relation.

## evidence_audit

- User correction evidence: the user stated that the overall architecture has no problem and that the first sentence should include both industry background and problem background.
- User example evidence: the user provided "超结构已被广泛应用于航空航天的防护中" as the intended type of industry background.
- Generated-output evidence: the previous abstract began with "超结构在冲击载荷下的变形模式、应力波传播路径和能量耗散机制共同决定其抗冲击性能", which states the problem relation but not the industry/application background.
- Related rule evidence: [[Abstract opening should connect application context to core relation]] supports using application context in the opening while immediately connecting to the core research relation.
- Unsupported inference handling: no specific industry beyond aerospace protection is generalized as mandatory, because the user only provided aerospace protection as an example.

## required_future_behavior

When writing a new abstract opening for superstructure impact, begin with a compact industry/application clause, then immediately connect to the impact-protection problem. Do not use a broad industry sentence that is disconnected from the research relation.

## no_regression_check

- First sentence includes industry/application background.
- First sentence also includes problem background or quickly transitions to it.
- The opening does not remain generic background.
- No invented quantitative results or unprovided validation data are added.
