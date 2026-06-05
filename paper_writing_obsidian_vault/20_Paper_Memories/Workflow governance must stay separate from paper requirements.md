---
title: Workflow governance must stay separate from paper requirements
tags:
  - layer/evidence
  - no-regression
  - paper-memory
  - workflow-governance
---

# Workflow governance must stay separate from paper requirements

## Problem Pattern

The self-growing paper-writing knowledge network can incorrectly summarize workflow logic as if it were a manuscript requirement. This pollutes later writing-rule application because rules about memory collection, automation, iteration, or knowledge-base maintenance may be mistaken for rules about abstract writing, introduction structure, claims, wording, or evaluation criteria.

## User Feedback

The user explicitly stated that the current knowledge base has a major problem: it can treat workflow logic as paper requirements during summarization.

## Reusable Rule

Workflow, automation, memory-management, and knowledge-base maintenance rules must be stored in a dedicated workflow-governance path and kept separate from paper-writing rules. They may guide how the knowledge base grows, but they must not be applied as manuscript requirements.

## Implementation Boundary

- Store intermediate paper-writing rules in `30_Writing_Rules`.
- Store workflow/process-governance rules in `35_Workflow_Governance`.
- Promote only paper-writing rules into `40_Final_Generalized_Rules`.
- Keep workflow-governance rules out of manuscript drafting checklists unless the task is explicitly about managing the knowledge base.

## Next Test

Before applying or promoting any rule, first label it as `paper_writing` or `process_governance`. Only `paper_writing` rules may constrain manuscript wording, section structure, claims, or evaluation criteria.
