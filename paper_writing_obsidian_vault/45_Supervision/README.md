---
title: Supervision layer
tags:
  - layer/reasoning
  - supervision
  - user-triggered
---

# Supervision Layer

This layer stores user-triggered supervision corrections.

It is not a scoring layer. It is started only by:

- active supervision: the user explicitly asks Codex to start the supervision system for a writing task;
- random supervision: the user says an old error or previously corrected problem has reappeared.

## Agent Responsibility

After a valid trigger, Codex handles the supervision workflow end to end:

1. identify the user correction or repeated-error claim;
2. retrieve related `45`, `40`, `50`, `60`, `30`, and when necessary `20` evidence;
3. analyze the error type and affected rules;
4. write the correction note here;
5. update the future no-regression requirement.

## Evidence Rule

Codex must not invent causes, rules, or corrections.

Every correction must cite concrete evidence from the user's correction text, the generated output being corrected, or related vault notes. Obsidian links may help find relationships, but links alone are not evidence.

Unsupported inferences must be removed or marked `needs_user_confirmation`.
