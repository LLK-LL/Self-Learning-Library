---
title: Word formula prose audit promoted to skill
tags:
  - formula-prose
  - layer/evidence
  - paper-memory
  - skill-promotion
  - workflow-governance
source: user_instruction
source_priority: user_high
status: active
scope: theory-formula, global-format, file-processing, knowledge-base-governance
---

# Word formula prose audit promoted to skill

## Memory Content

Formula-neighbouring Word prose has repeatedly produced high-cost regressions in
this project: raw underscore notation remained in manuscript prose, Greek
symbols were replaced by English placeholders, numeric and label-like indices
needed upright formatting, variable bodies needed italic formatting, and
formatting rationale was accidentally written into article body text.

This pattern is now stable enough to become the narrow
`word-formula-prose-audit` skill. The skill should audit run/XML-level Word
formatting for prose symbols, not just formula objects.

## Reusable Rule

For Word outputs with formula explanations, use a dedicated formula-prose audit:
check raw notation, real Word subscript/superscript runs, italic/upright
classification, Greek placeholder replacement, and manuscript-body purity.

## Boundary

This skill governs DOCX processing and verification. It does not replace
paper-writing rules about what symbols mean, and it does not replace
`docx-omml-repair` for damaged OMML formula objects.
