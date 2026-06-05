---
title: Manuscript content must be confirmed in chat before Word insertion
created: 2026-06-05 10:55
tags:
  - G11
  - layer/reasoning
  - rule-type/process_governance
  - workflow-governance
---

# Manuscript content must be confirmed in chat before Word insertion

## Rule Type

- `process_governance`

## Governance Rule

For user-requested manuscript-content changes, Codex must first provide the proposed revised content in chat and wait for user confirmation before writing that content into Word. This guards against unwanted DOCX edits while still allowing file inspection, formatting checks, RAG, and knowledge-base maintenance before confirmation.

## Boundary

- This rule governs the knowledge-base workflow only.
- It must not be treated as a manuscript claim, section-structure requirement, wording rule, or paper evaluation criterion.

## Evidence Memories

- [[User confirmed clean theory formula Word output as future basis]]
- [[User preference - chat first before Word insertion]]
- [[Abstract rule - earlier industry background constraint]]
- [[DOCX terminology unification and Windows processing pitfalls]]
- [[Supervision non-Newtonian formula Word output followed confirmed baseline]]
- [[User confirmed hyperelastic theory formula Word baseline]]

## Governance Test

Before writing revised manuscript wording into a DOCX, check whether the user has approved the chat version; if not, provide the proposed content in chat and stop before Word insertion.
