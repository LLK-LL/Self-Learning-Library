---
title: 2026-06-03 SCI-memory workflow 10-40-20-80 update
tags:
  - layer/evidence
  - paper-revision
  - workflow-update
---

# 2026-06-03 SCI-memory workflow 10-40-20-80 update

## Change Points

- The user redefined the paper-writing knowledge flow so ordinary `SCI-memory` use must first record concrete eligible content in `10_Project_Change_Log`, then promote reusable evidence into `40_Paper_Memories`, and then summarize the new evidence into `20_Writing_Rules`.
- Manual iteration should no longer stop at `20_Writing_Rules`; it should summarize current `20_Writing_Rules` into `80_Final_Generalized_Rules`.
- Unresolved contradictions remain in `50_Conflicts`.
- Rules that still have insufficient evidence for stable generalization should be held separately in `65_Limited_Rules`.
- `60_Hypotheses` must remain as an independent hypothesis layer and must not be repurposed.
- The `SCI-memory` skill should directly load the latest final writing rules from `80_Final_Generalized_Rules` when drafting or revising.
- Existing guardrails remain unchanged: mentor-sourced evidence keeps higher priority, and all summarization must stay evidence-grounded without unsupported invention.

## Evidence Memories

- [[SCI-memory workflow rule - record to 10 and 40, refresh 20, iterate to 80]]
