# Full Rule Iteration

Use full iteration when you want the harness to inspect the broader evidence graph and decide which lessons are stable, limited, conflicting, or outdated.

## When to Use

Run full iteration when the user asks for:

- self-iteration;
- final generalization;
- screening;
- rule promotion;
- conflict detection;
- a complete refresh of stable rules.

Do not run it automatically for every ordinary task. Lightweight retrieval is cheaper and usually enough.

## Command

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\run_paper_iteration.ps1
```

The script calls:

```powershell
tools\paper_iteration.py --root <project-root>
```

## Outputs

Latest reports are written under:

```text
paper_writing_obsidian_vault/70_Iterative_Thinking/
```

Typical outputs include:

- generated conclusions;
- graph analysis;
- candidate rules;
- latest iteration JSON;
- stable/limited/conflicting rule summaries.

## Reporting Pattern

After a full iteration, report:

- stable rules promoted;
- limited rules that need scope boundaries;
- unresolved conflicts;
- evidence strength;
- suggested next action.
