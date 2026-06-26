---
title: Skill promotion registry
created: 2026-06-26 17:13
tags:
  - layer/reasoning
  - skill-promotion
  - workflow-governance
---

# Skill Promotion Registry

This registry tracks repeated paper-workflow knowledge that may be promoted into Codex skills. It is a workflow-governance artifact, not a manuscript-writing rule layer.

## Active Skills

### paper-kb-governance

- Stage: `P3 active skill`
- Trigger: maintaining a paper-writing knowledge base, separating writing rules from workflow governance, auditing evidence boundaries, or deciding whether repeated paper-workflow memories should become skills.
- Source notes:
  - [[KB RAG should retrieve selectively and preserve evidence boundaries]]
  - [[Workflow governance must stay separate from paper requirements]]
  - [[Process governance must not become manuscript requirements]]
  - [[Repeated workflow knowledge may be promoted to skills]]
- Validation:
  - ordinary manuscript-writing RAG excludes workflow governance; promotion candidates cite source notes and preserve original evidence.

### word-formula-prose-audit

- Stage: `P3 active skill`
- Trigger: checking Word DOCX formula-neighbouring prose for true subscript/superscript runs, italic/upright symbol typography, raw notation, Greek placeholders, or formatting-rationale contamination.
- Source notes:
  - [[Formula symbols in prose must match formula typography]]
  - [[User correction - prose formula symbols require real formatting]]
  - [[User correction - do not put formatting rationale into manuscript body]]
  - [[Professional Word formulas require post-BuildUp layout audit]]
  - [[2026-06-06 SPH-FEM formula professional-format regression]]
- Validation:
  - no raw underscore/caret notation remains; run-level XML confirms true subscript/superscript and italic/upright rules; manuscript body contains no audit wording.

## Existing Related Skills

### docx-omml-repair

- Stage: `P3 active skill`
- Trigger: repairing or generating DOCX files with OMML equations, damaged math symbols, formula layout issues, or Windows Unicode encoding risks.
- Boundary:
  - use it for formula-object repair;
  - use `word-formula-prose-audit` for manuscript prose around formulas.

## Candidate Backlog

### project-script-reuse-before-new-script

- Stage: `P1 promotable`
- Trigger: a project task appears to need a new helper script.
- Source notes:
  - [[Before creating scripts retrieve and reuse local scripts]]
  - [[KB RAG should retrieve selectively and preserve evidence boundaries]]
- Current decision:
  - keep as project workflow governance for now;
  - promote only if the same script-reuse flow becomes useful across multiple projects.

## Codex Candidate Queue

- No Codex-maintained skill candidates recorded yet.

## Current Process-Governance Source

- [[Before creating scripts retrieve and reuse local scripts]]
- [[DOCX edit scope must be verified before manuscript changes]]
- [[Manuscript content must be confirmed in chat before Word insertion]]
- [[Mentor advice has higher priority in paper-memory reasoning]]
- [[Process governance must not become manuscript requirements]]
- [[Project root must expose mandatory harness entrypoint]]
- [[RAG retrieval should be a selective loading layer]]
- [[Repeated workflow knowledge may be promoted to skills]]
- [[Word formula prose audit should run as a narrow skill]]
- [[Writing knowledge should become reusable process memory]]
