---
title: Mandatory RAG startup and repair
supervision_mode: user_directive
trigger: explicit_user_rule
correction_type:
  - workflow_governance
  - rag_startup
priority: highest
status: active
tags:
  - highest-priority
  - knowledge-base-governance
  - layer/reasoning
  - rag
  - supervision
---

# Mandatory RAG Startup And Repair

## User Directive

On 2026-06-06, the user added a highest-priority project knowledge-base rule:

- knowledge-base retrieval must enable RAG;
- if RAG has a startup or execution problem, Codex must repair RAG first;
- the repair method must be recorded;
- next time, Codex must directly use the recorded working method to start RAG.

## Highest-Priority Rule

For any task in this project that requires knowledge-base retrieval, writing-rule application, script-reuse checking, workflow-governance lookup, or paper-memory consultation, Codex must attempt local RAG first.

RAG must be used as a low-token retrieval layer by default: retrieve compact task-relevant summaries first, load only the matched notes or excerpts needed for the current task, and avoid full-vault scanning unless RAG repair fails or the user explicitly requests broad/final review.

RAG failure is not permission to silently fall back to broad manual scanning. If RAG fails, first diagnose and repair the startup path, then record the repair method in the project knowledge base before proceeding.

## Recorded Working Startup Method

Use PowerShell through RTK from the project root:

```powershell
rtk powershell -NoProfile -Command "py tools\kb_rag.py --query '<query>' --limit 3"
```

For workflow-governance queries, use:

```powershell
rtk powershell -NoProfile -Command "py tools\kb_rag.py --query '<query>' --include-workflow --limit 3"
```

This method is preferred because it resolves the local Windows Python launcher correctly. A previous direct call through `rtk py ...` returned `No installed Python found!` in one execution context, while the PowerShell-wrapped `py tools\kb_rag.py ...` path succeeded.

## Required Failure Handling

If RAG fails:

1. Check Python launcher availability with:
   `rtk powershell -NoProfile -Command "py --version; python --version; Get-Command py -ErrorAction SilentlyContinue; Get-Command python -ErrorAction SilentlyContinue"`
2. Retry RAG with the recorded PowerShell-wrapped startup method above.
3. If a new fix is required, record the exact failure, command, repair method, and successful verification in `45_Supervision` or `35_Workflow_Governance` before continuing.
4. Do not continue with unbounded vault loading unless the user explicitly permits emergency fallback or RAG is genuinely unavailable after repair attempts.

## Scope Boundary

This rule governs project workflow and knowledge-base operation only. It must not be inserted into manuscript prose or treated as a scientific writing claim.

## Verification Evidence

The recorded method was verified on 2026-06-06 with:

```powershell
rtk powershell -NoProfile -Command "py tools\kb_rag.py --query 'RAG mandatory highest priority startup repair method' --include-workflow --limit 3"
```

The command completed successfully and produced a RAG token-savings report.
