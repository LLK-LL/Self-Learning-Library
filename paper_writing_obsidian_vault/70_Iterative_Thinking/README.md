---
title: Paper Iteration Automation
tags:
  - automation
  - layer/output
  - memory-grounded
  - paper-iteration
---

# Paper Iteration Automation

## Manual Start

Use the Codex manual automation named `论文证据迭代思考（手动启动）`.

The automation runs:

```powershell
powershell -ExecutionPolicy Bypass -File .\run_paper_iteration.ps1
```

## What It Does

1. Reads existing paper memory notes from `20_Paper_Memories`.
2. Parses vault `[[wikilinks]]` and frontmatter tags as a layered local note graph.
3. Maintains frontmatter layer tags: `layer/evidence`, `layer/reasoning`, and `layer/output`.
4. Generates intermediate paper-writing rules in `30_Writing_Rules`.
5. Writes workflow and process-governance rules in `35_Workflow_Governance`.
6. Promotes sufficiently generalized paper-writing rules into `40_Final_Generalized_Rules`.
7. Lists unresolved contradictions in `50_Conflicts`.
8. Preserves still-limited paper-writing rules in `60_Limited_Rules`.
9. Writes the current iteration, graph analysis, and `layered_graph_overview.md` under `70_Iterative_Thinking`.
10. Optionally validates Codex semantic rule candidates from `70_Iterative_Thinking/codex_candidate_rules.json` before writing them into the proper layer.

## Evidence Rule

Every conclusion must cite existing notes in `20_Paper_Memories` and may use current workspace files only as auxiliary evidence. Vault graph links are structural support only; they do not replace note content evidence. Only `20_Paper_Memories` and `10_Project_Change_Log` belong to the Evidence Graph used for scoring. Reasoning and output layers are audit context only. This automation does not import from the local memory database. The process must not use outside knowledge unless the user explicitly asks for it.

## Obsidian Graph Groups

Use these group filters in Obsidian graph view:

- Evidence: `tag:#layer/evidence`
- Reasoning: `tag:#layer/reasoning`
- Output: `tag:#layer/output`

Use this graph search filter to show only layered knowledge-base nodes:

```text
tag:#layer/evidence OR tag:#layer/reasoning OR tag:#layer/output
```

## Expected Report

After a manual run, report back to the user in this order:

1. Final generalized paper-writing rules from `40_Final_Generalized_Rules`.
2. Limited rules currently held in `60_Limited_Rules`.
3. Workflow/process-governance rules from `35_Workflow_Governance`, explicitly marked as not manuscript requirements.
4. Evidence Graph support strength and structurally isolated evidence notes.
5. Contradictions or unresolved conflicts that require user judgment.
6. The next most concrete writing improvement or validation action.
