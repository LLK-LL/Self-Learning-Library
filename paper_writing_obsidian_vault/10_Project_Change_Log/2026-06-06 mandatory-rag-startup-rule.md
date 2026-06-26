---
title: 2026-06-06 mandatory-rag-startup-rule
created: 2026-06-06
tags:
  - knowledge-base-governance
  - layer/evidence
  - rag
  - workflow
---

# Mandatory RAG Startup Rule

## Change

Added the user's highest-priority workflow rule requiring project knowledge-base retrieval to use RAG first.

## User Directive

The user required:

- knowledge-base content priority should be highest;
- knowledge-base retrieval must enable RAG;
- if RAG has a problem, repair it first;
- record the solution;
- next time, directly use the recorded startup method.

## Recorded Working Method

Use:

```powershell
rtk powershell -NoProfile -Command "py tools\kb_rag.py --query '<query>' --limit 3"
```

For workflow-governance:

```powershell
rtk powershell -NoProfile -Command "py tools\kb_rag.py --query '<query>' --include-workflow --limit 3"
```

## Evidence

The PowerShell-wrapped RAG command succeeded after a direct `rtk py ...` call had previously produced `No installed Python found!` in one context.

## Linked Rules

- [[Mandatory RAG startup and repair]]
- [[Mandatory RAG startup and repair before fallback]]
