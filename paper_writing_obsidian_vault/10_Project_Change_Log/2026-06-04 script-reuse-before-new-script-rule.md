---
title: 2026-06-04 script reuse before new script rule
created: 2026-06-04 19:44
tags:
  - layer/evidence
  - script-reuse
  - token-savings
  - workflow
---

# 2026-06-04 Script Reuse Before New Script Rule

## User Instruction

The user requested a new rule for the paper knowledge base: when a task appears to require creating a new script, Codex should first use the already deployed RAG method to check whether suitable local scripts already exist. If a suitable script exists, Codex should reuse it directly or make a small modification, with token savings as the main purpose.

## RAG Check

Before writing the rule, local RAG was run with:

`py tools\kb_rag.py --query "新建脚本前 检索 已有脚本 RAG token 节省 复用 小改" --include-workflow --limit 8`

The closest existing rule was `35_Workflow_Governance/RAG retrieval should be a selective loading layer.md`, which covers selective knowledge retrieval but not the specific script-reuse requirement. The RAG report estimated an 86.9% token saving for this workflow-governance query.

## Result

A new reusable workflow-governance memory was added to `20_Paper_Memories`, and `tools/paper_iteration.py` was updated so the rule can be regenerated into `35_Workflow_Governance`.
