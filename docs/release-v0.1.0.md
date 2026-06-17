# v0.1.0 - Local self-learning knowledge-base harness

Self-Learning Library v0.1.0 introduces the first public shape of a local-first knowledge-base harness for AI-assisted work.

## What is included

- A layered Obsidian-compatible Markdown vault.
- Codex-facing root instructions in `AGENTS.md`.
- A project harness workflow in `PROJECT_HARNESS_WORKFLOW.md`.
- Lightweight local retrieval with `tools/kb_rag.py`.
- Full graph-style iteration and rule promotion with `tools/paper_iteration.py`.
- PowerShell entrypoint `run_paper_iteration.ps1`.
- Example exported manuscript-assistance vault.
- Documentation for lightweight retrieval, full iteration, no-regression guards, and domain adaptation.
- Security and publishing guidance.

## Who should try it

This project is useful if you want an AI assistant to:

- retrieve relevant rules before a task;
- avoid repeating past mistakes;
- separate concrete evidence from stable rules;
- detect unresolved conflicts;
- promote repeated lessons into reusable knowledge;
- keep a local, inspectable, file-backed memory structure.

## Current limitations

- The included vault comes from a paper-writing workflow, although the mechanism is domain-independent.
- Convenience scripts are Windows/PowerShell-first.
- Windows users should enable Git long paths and clone into a short local path because the example vault contains descriptive long note filenames.
- The repository currently includes a real exported example vault, so users should review privacy and publishing guidance before adapting the pattern.
- Retrieval and rule promotion are intentionally simple and local-first.

## Suggested repository description

```text
Local-first self-learning knowledge-base harness for AI agents. Retrieve rules, avoid regressions, and promote repeated lessons into stable reusable knowledge.
```

## Suggested topics

```text
ai-agent, ai-memory, knowledge-base, self-learning, local-first, codex, rag, obsidian, markdown, workflow, research, writing, automation, python
```
