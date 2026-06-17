# Build a Domain-Specific Vault

The included vault is from a manuscript-assistance project, but the layered pattern can be adapted to other domains.

## Reusable Layer Pattern

```text
10_Project_Change_Log     -> concrete events and changes
20_Domain_Memories        -> reusable lessons and preferences
30_Domain_Rules           -> intermediate rules
35_Workflow_Governance    -> process rules for the harness
40_Final_Generalized_Rules -> stable reusable rules
45_Supervision            -> high-priority corrections and no-regression constraints
50_Conflicts              -> unresolved contradictions
60_Limited_Rules          -> useful but scoped rules
70_Iterative_Thinking     -> generated reports and conclusions
```

## Example Domains

| Domain | What memories might contain |
| --- | --- |
| Coding | project conventions, recurring bugs, test commands, review preferences |
| Research | citation habits, screening criteria, writing moves, analysis pitfalls |
| Product | customer insights, roadmap decisions, launch lessons, support patterns |
| Lab workflows | instrument procedures, failure modes, calibration rules, safety notes |
| Legal drafting | clause preferences, review checklists, jurisdiction-specific caveats |
| Personal SOPs | recurring admin workflows, automation commands, decision rules |

## Adaptation Steps

1. Copy the repository.
2. Replace the vault notes with your own domain notes.
3. Rename folders if useful.
4. Update vault constants in:
   - `tools/kb_rag.py`
   - `tools/paper_iteration.py`
   - `PROJECT_HARNESS_WORKFLOW.md`
5. Update `AGENTS.md` so your agent knows when to trigger the harness.
6. Run lightweight retrieval before ordinary tasks.
7. Run full iteration only when you want rule promotion or conflict screening.

## Keep the Layers Separate

Do not mix process rules with output content. A rule about how the assistant should verify work should guide generation, not appear in the final document, code, or report.
