---
title: Memory destination wording should distinguish total memory from project knowledge base
created: 2026-06-05 12:45
tags:
  - layer/evidence
  - memory-routing
  - paper-memory
  - workflow-governance
source: user_correction
priority: user_high
---

# Memory destination wording should distinguish total memory from project knowledge base

## Problem Pattern

In this workspace, an unqualified memory request can be misrouted into the local paper knowledge base even when the user meant total memory only. That causes workflow confusion and can pollute the project knowledge base with records the user did not intend to store there.

## User Feedback

The user explicitly clarified the routing rule: when the user says something whose meaning is "write/save to memory", it should mean total memory by default. Only wording that explicitly means "record to the project knowledge base" should route content into this paper-writing knowledge base.

## Reusable Rule

Before recording anything in this workspace, first disambiguate the destination:

- unqualified memory wording -> total memory only;
- explicit project-knowledge-base wording -> local paper knowledge base;
- explicit project workflow rule requests -> store the rule as workflow-governance material, not manuscript-writing content.

## Implementation Boundary

- Apply this rule before any write-back into `paper_writing_obsidian_vault`.
- Keep this as workflow-governance logic, not a manuscript-writing rule.
- Do not silently mirror unqualified total-memory requests into the local paper knowledge base.

## Next Test

If the user says only "write this to memory", do not record it in the project knowledge base. If the user explicitly says "record this to the project knowledge base" or asks to put a rule into the project workflow, update the local harness records.
