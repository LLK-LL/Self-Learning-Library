---
title: Project Harness Workflow
created: 2026-06-04
tags:
  - harness
  - workflow
  - paper-writing
  - project-local
---

# Project Harness Workflow

## Status

This harness is enforced at the project root. It is the primary workflow for paper-writing work in this project.

`SCI-memory` remains available only as a fallback or external reusable skill. The project harness owns the normal workflow inside this workspace.

Any request that changes article/manuscript content, asks Codex to write paper content, records paper-writing knowledge, extracts writing rules, or performs final rule iteration inside this project must use this harness.

When this harness is triggered, three functions are automatically active by default:

1. writing-rule application
2. no-regression guard
3. collection workflow

Final summarization and final generalization are not automatic. They run only when the user explicitly asks for final summarization, final generalization, iteration, or screening.

## Knowledge Base Paths

Use these local paths:

- `paper_writing_obsidian_vault/00_Index.md`
- `paper_writing_obsidian_vault/10_Project_Change_Log`
- `paper_writing_obsidian_vault/20_Paper_Memories`
- `paper_writing_obsidian_vault/30_Writing_Rules`
- `paper_writing_obsidian_vault/35_Workflow_Governance`
- `paper_writing_obsidian_vault/40_Final_Generalized_Rules`
- `paper_writing_obsidian_vault/45_Supervision`
- `paper_writing_obsidian_vault/50_Conflicts`
- `paper_writing_obsidian_vault/60_Limited_Rules`
- `paper_writing_obsidian_vault/70_Iterative_Thinking`

## Writing Rule Application

This function is automatically active whenever the harness is triggered.

Use lightweight local RAG before loading rule content:

1. Search `45_Supervision`, `40_Final_Generalized_Rules`, `50_Conflicts`, `60_Limited_Rules`, then `30_Writing_Rules`.
2. Load only matched notes or excerpts when feasible.
3. Expand to `20_Paper_Memories` only through matched evidence links when high-risk verification requires it.
4. Convert retrieved rules into a short task checklist before revising manuscript text.

Use `tools/kb_rag.py` when a scripted local RAG retrieval is useful.

Default token-saving call for ordinary manuscript-writing tasks:

```powershell
py tools\kb_rag.py --query "<task keywords>" --limit 3
```

Do not add `--include-workflow`, `--include-evidence`, or `--include-related` for ordinary writing tasks. `35_Workflow_Governance` is for workflow/governance questions only. `20_Paper_Memories` should be expanded only when high-risk verification requires evidence. `70_Iterative_Thinking` must not be loaded as ordinary task context; read only targeted excerpts when the user explicitly asks for iteration, screening, final summarization, final generalization, or audit.

## Source Priority And Scope

When rules or memories conflict, resolve them by source priority and application scope, not by folder order alone.

Priority order:

1. explicit mentor feedback;
2. active user-triggered supervision corrections;
3. user-confirmed successful output baselines and explicit user corrections;
4. ordinary paper memories;
5. change-log facts;
6. generated intermediate or final rules without newer correction evidence.

Every high-priority rule should state its application scope where possible, such as `abstract`, `introduction`, `theory-formula`, `global-format`, `file-processing`, `script-workflow`, or `knowledge-base-governance`. A high-priority rule must be applied only inside its scope unless the user explicitly makes it global.

This scope boundary is required to prevent manuscript body contamination: workflow, audit, formatting rationale, file-processing, and script rules may control generation and checking, but they must not be written into article prose.

## No-Regression Guard

This function is automatically active whenever the harness is triggered.

Before closing a manuscript-writing task, verify the requested scope and check for regressions against the user's explicit constraints. For DOCX formula work, check formula text, visible prose, and run-level formatting when relevant.

## Manuscript Body Purity Guard

This guard is active for all manuscript/article/Word output tasks.

Manuscript body text must contain only the intended article content. Do not write Codex reasoning, formatting audit logic, workflow notes, rule explanations, or self-check statements into the manuscript body. For formula symbol explanations, explain only the symbol meaning. Statements such as "the subscript is numeric", "should remain upright", "should be italic", "checked by audit", or similar formatting rationale belong only in reports, verification notes, or the knowledge base, never in the Word body text.

Before finalizing a Word/DOCX output, run a visible-prose no-regression check for meta-process wording, including formatting rationale and self-check language. If such wording appears, rewrite the prose and regenerate the DOCX before reporting completion.

## Chat-First Word Insertion Guard

This guard is active for user-requested manuscript-content changes.

Before writing revised wording into Word/DOCX, Codex must first provide the proposed revised content in the chat and wait for user confirmation. This applies to paragraph rewrites, section rewrites, formula-description rewrites, translations or polishing intended for the manuscript, and any newly drafted content that would replace or enter a Word manuscript file.

Allowed before confirmation:

- inspect files;
- run local RAG;
- check formatting;
- draft proposed text in chat;
- update knowledge-base workflow records when the user asks to add a rule.

Not allowed before confirmation:

- insert unapproved revised wording into `manuscript.docx` or another Word manuscript file;
- overwrite Word manuscript content with a new draft.

If the user explicitly says to write directly into Word without preview, that newer instruction controls for that task.

## Script Reuse Guard

This guard is active whenever a project task appears to require a new helper script.

Purpose: save tokens by avoiding unnecessary re-derivation and one-off script creation.

Required steps:

1. Run local RAG for workflow/tooling context, for example:
   `py tools\kb_rag.py --query "<task keywords> existing script reuse token savings" --include-workflow`
2. Search existing script inventory with `rg --files` and targeted `rg -n` searches under `tools`, `process_files_*`, and relevant project folders.
3. Inspect only the most relevant candidate scripts.
4. Reuse an existing script directly when it already covers the task.
5. Prefer a small scoped modification when the existing script is close and the change does not risk unrelated behavior.
6. Create a new script only when no safe local candidate exists, or modifying an existing script would create higher regression risk.
7. State in the final response or change log whether the task reused, patched, or newly created a script and why.

## Collection Workflow

This function is automatically active whenever the harness is triggered.

Route records as follows:

1. concrete modification process -> `10_Project_Change_Log`
2. suggestions, preferences, reusable lessons, and mentor feedback -> `20_Paper_Memories`
3. explicit user-declared rules or stable intermediate rules -> `30_Writing_Rules`

If nothing reusable exists, state that nothing was collected.

After collection, run the root-level harness entrypoint:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\run_paper_iteration.ps1
```

## Entrypoint

The project root must contain `run_paper_iteration.ps1`. That script must execute:

```powershell
tools\paper_iteration.py --root <project-root>
```

Do not use the archived copy under `process_files_20260604` as the active entrypoint.
