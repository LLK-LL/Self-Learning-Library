---
title: Before creating scripts retrieve and reuse local scripts
created: 2026-06-04 19:44
tags:
  - layer/evidence
  - script-reuse
  - token-savings
  - workflow-governance
source: user_instruction
priority: user_high
---

# Before Creating Scripts Retrieve And Reuse Local Scripts

When a task seems to require a new helper script, Codex should first search the local project for an existing script that can complete the task or be adapted with a small change. The primary purpose is token savings: reusing a tested local script avoids re-deriving logic, re-reading large files, and generating unnecessary one-off code.

Required workflow:

1. Use the deployed local RAG method first for workflow/tooling context, for example:
   `py tools\kb_rag.py --query "<task keywords> existing script reuse token savings" --include-workflow`
2. Search local script inventory with fast filename/content search, focusing on `tools`, `process_files_*`, and relevant vault notes:
   `rg --files | rg "keyword|script-name|task-area"`
   `rg -n "keyword|function|docx|equation|rag" tools process_files_*`
3. Inspect only the most relevant candidate scripts. Do not load every script unless the shortlist is unclear.
4. Prefer direct reuse when an existing script already covers the task.
5. Prefer small modification of an existing script when the needed change is narrow and does not risk unrelated behavior.
6. Create a new script only when no suitable local script exists, the closest script is unsafe or too specialized, or modifying it would create higher regression risk.
7. In the final response or change log, state whether the task reused, patched, or newly created a script and why.

Boundary: this is a workflow/token-saving rule. It should not block manuscript edits when the task can be completed safely without a script, and it should not force risky modification of an existing script merely to avoid creating a new file.

Evidence: [[2026-06-04 script reuse before new script rule]]
