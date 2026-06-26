Project-local mandatory workflow: follow [PROJECT_HARNESS_WORKFLOW.md](./PROJECT_HARNESS_WORKFLOW.md) for paper-writing work in this workspace.

This project defaults to the local harness. `SCI-memory` remains a fallback skill, not the primary workflow.

Required behavior:

- Use the local harness for writing-rule application, no-regression checks, paper-memory collection, and rule-layer iteration.
- Codex owns all project knowledge-base maintenance in this workspace, including RAG health checks, orphan-note checks, index checks, iteration, conflict monitoring, and skill-promotion review. Do not route these tasks to Hermes/Jarvis or ask the user to summon Hermes for knowledge-base maintenance.
- Trigger the harness for any request that changes article/manuscript content, asks Codex to write or revise paper content, records paper-writing knowledge, extracts writing rules, or performs final rule iteration inside this project.
- When the harness is triggered, automatically run writing-rule application, no-regression guard, and collection workflow before the final response.
- In this workspace, an unqualified request whose meaning is "save/write to memory" means total memory, not the local paper knowledge base. Only explicit requests whose meaning is "record to the project knowledge base" or "record to the paper knowledge base" should write into the project paper knowledge base.
- For any user-requested manuscript-content change, provide the proposed revised content in the chat first and wait for user confirmation before writing that wording into Word/DOCX; file inspection, RAG, formatting checks, and knowledge-base maintenance may still run before confirmation.
- Writing-rule application must use lightweight local RAG by default: retrieve task-relevant rules first with `py tools\kb_rag.py --query "<task keywords>" --limit 3`, load only matched rules or excerpts when feasible, and reserve full rule-layer scanning for explicit final summarization, final generalization, iteration, screening, or automation.
- For ordinary writing tasks, do not add `--include-workflow`, `--include-evidence`, or `--include-related`; do not load `70_Iterative_Thinking` as task context.
- Run the no-regression guard when the user asks to write, rewrite, polish, translate, restructure, expand, shorten, replace, or evaluate article/manuscript/paper text, including Chinese expression polishing.
- Before creating a new helper script for a project task, use local RAG and fast script search to check whether an existing script can be reused directly or with a small scoped modification; prefer reuse for token savings and record why a new script is necessary if one is created.
- Collection follows `10 -> 20 -> 30` by default whenever the harness is triggered; if nothing reusable exists, state that nothing was collected.
- Automation follows `30 -> 50 / 60 / 40` only when the user asks for iteration, screening, final summarization, or final generalization.
- Use `SCI-memory` only as a fallback if the project harness is unavailable or the user explicitly asks for that skill.
