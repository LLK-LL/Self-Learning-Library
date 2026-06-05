---
title: SCI-memory workflow rule - record to 10 and 40, refresh 20, iterate to 80
tags:
  - SCI-memory
  - layer/evidence
  - paper-memory
  - workflow-rule
---

# SCI-memory workflow rule - record to 10 and 40, refresh 20, iterate to 80

## Problem pattern

The previous workflow let the iteration output expose conclusions that were still too close to raw memory evidence, and it did not separate intermediate rule summaries from final generalized rules strongly enough.

## Revision action

When `SCI-memory` is used or the user explicitly asks to record paper-writing knowledge:

- first capture concrete eligible change content in `10_Project_Change_Log`,
- promote reusable evidence into `40_Paper_Memories`,
- summarize the newly added `40_Paper_Memories` evidence into `20_Writing_Rules`.

When the user manually starts iteration:

- summarize current `20_Writing_Rules` into `80_Final_Generalized_Rules`,
- keep unresolved contradictions in `50_Conflicts`,
- keep still-limited rules in `65_Limited_Rules`,
- preserve `60_Hypotheses` as a separate layer,
- and sync the final generalized rules back into the `SCI-memory` skill so drafting uses the latest stable rule set.

## Potential generalized rule

In a paper-writing knowledge base, raw evidence, intermediate rule summaries, final generalized rules, unresolved conflicts, hypotheses, and still-limited rules should be separated into distinct layers so drafting uses only the most stable rule layer while evidence remains auditable.

## Evidence

- User instruction on 2026-06-03 redefining the SCI-memory workflow and explicitly preserving mentor-priority and evidence-grounded reasoning constraints.

## Applicability

- Obsidian-based paper-writing knowledge bases that grow from revision evidence into reusable writing rules.
- Workflows where the writing skill should apply only the latest stable generalized rule set during drafting or revision.

## Boundary

- This rule does not remove the need to keep concrete project edits in `10_Project_Change_Log`.
- This rule does not allow unsupported generalization; promotion into `80_Final_Generalized_Rules` must still be evidence-grounded.
- This rule does not change the existing higher priority of mentor-sourced evidence.
