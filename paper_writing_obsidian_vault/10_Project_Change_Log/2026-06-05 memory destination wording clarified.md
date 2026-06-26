---
title: 2026-06-05 memory destination wording clarified
created: 2026-06-05 12:41
tags:
  - knowledge-base-governance
  - layer/evidence
  - memory-routing
  - user-instruction
  - workflow
---

# 2026-06-05 Memory Destination Wording Clarified

## User Instruction

The user clarified a routing convention for future requests in this workspace:

- when the user uses unqualified wording whose meaning is "save/write to memory", it means total memory;
- only explicit project-knowledge-base wording should route content into this paper knowledge base.

## Rule Meaning

- Unqualified memory requests must not silently write into `paper_writing_obsidian_vault`.
- Explicit project workflow or project knowledge-base requests should still update the local harness records.
- This is a workflow-governance routing rule, not a manuscript-writing rule.

## Existing Related Rule

The closest previous governance rule was `Process governance must not become manuscript requirements`, which separates process rules from manuscript constraints. The new rule is narrower: it decides the destination of memory requests before any local knowledge-base write-back happens.
