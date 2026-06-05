---
title: Codex manual analysis prompt latest
tags:
  - automation
  - layer/output
  - paper-iteration
---

# Codex Manual Analysis Prompt

Use the current project directory and existing `20_Paper_Memories` notes only.

- Iteration JSON: `F:\Users\Administrator\Desktop\Self-Learning-Library-publish\paper_writing_obsidian_vault\70_Iterative_Thinking\iteration_20260605_105542.json`
- Latest conclusions: `F:\Users\Administrator\Desktop\Self-Learning-Library-publish\paper_writing_obsidian_vault\70_Iterative_Thinking\conclusions_latest.json`
- Codex candidate rules: `F:\Users\Administrator\Desktop\Self-Learning-Library-publish\paper_writing_obsidian_vault\70_Iterative_Thinking\codex_candidate_rules.json`
- Existing paper memory notes: `F:\Users\Administrator\Desktop\Self-Learning-Library-publish\paper_writing_obsidian_vault\20_Paper_Memories`
- Intermediate writing rules: `F:\Users\Administrator\Desktop\Self-Learning-Library-publish\paper_writing_obsidian_vault\30_Writing_Rules`
- Workflow/process-governance rules: `F:\Users\Administrator\Desktop\Self-Learning-Library-publish\paper_writing_obsidian_vault\35_Workflow_Governance`
- Final generalized rules: `F:\Users\Administrator\Desktop\Self-Learning-Library-publish\paper_writing_obsidian_vault\40_Final_Generalized_Rules`
- Supervision corrections: `F:\Users\Administrator\Desktop\Self-Learning-Library-publish\paper_writing_obsidian_vault\45_Supervision`
- Conflicts: `F:\Users\Administrator\Desktop\Self-Learning-Library-publish\paper_writing_obsidian_vault\50_Conflicts`
- Limited rules: `F:\Users\Administrator\Desktop\Self-Learning-Library-publish\paper_writing_obsidian_vault\60_Limited_Rules`
- Layered graph overview: `F:\Users\Administrator\Desktop\Self-Learning-Library-publish\paper_writing_obsidian_vault\70_Iterative_Thinking\layered_graph_overview.md`
- Obsidian graph groups: `tag:#layer/evidence`, `tag:#layer/reasoning`, `tag:#layer/output`

Tasks:

1. Verify every generalized conclusion against its listed memory evidence.
2. Use `graph_analysis_latest.md` to inspect layered structural support from vault `[[wikilinks]]` and frontmatter tags.
3. Treat mentor-sourced notes (`Source: mentor` or `Source Priority: mentor_high`) as higher-weight evidence than self-authored preferences when conclusions or conflicts disagree.
4. Report the final generalized paper-writing rules from `40_Final_Generalized_Rules` first so the user can review the latest writing constraints.
5. Report workflow/process-governance rules from `35_Workflow_Governance` separately and explicitly mark them as not manuscript requirements.
6. Report the still-limited rules from `60_Limited_Rules` separately from the final generalized rules.
7. Reject or flag any conclusion not supported by memory or current workspace files.
8. List contradictions that cannot be unified after source-priority handling and explicitly ask the user to resolve them.
9. Propose the next concrete writing improvement or validation step after the contradictions section.

Constraint: graph links are structural support only, not evidence by themselves. Only Evidence Graph links may affect support strength. Do not use outside knowledge unless the user explicitly asks for web or literature search.

Candidate rule schema:

```json
{
  "candidate_rules": [
    {
      "id": "C1",
      "title": "Short rule title",
      "category": "paper_writing",
      "conclusion": "Generalized rule text.",
      "evidence_notes": ["Exact 20_Paper_Memories note title"],
      "next_test": "Concrete validation test.",
      "rationale": "Why Codex proposed this rule."
    }
  ]
}
```
