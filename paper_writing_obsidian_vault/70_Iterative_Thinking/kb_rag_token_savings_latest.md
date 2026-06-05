---
title: KB RAG token savings latest
created: 2026-06-04 12:33
tags:
  - kb-rag
  - layer/output
  - token-savings
---

# KB RAG Token Savings

## Summary

- Queries: `1`
- Baseline tokens: `4830`
- RAG tokens: `5460`
- Tokens saved: `0`
- Savings: `0.0%`

## Method

- Baseline loads every Markdown note from the allowed knowledge-base layers.
- RAG first returns compact summaries, then selectively loads only chosen primary full vault notes.
- `related_ids` are retained as optional follow-up links but are not loaded by default.
- Token counts are estimated as `len(text) // 4`, matching the local recall-mode approximation.
- Workflow governance is excluded from paper-writing queries and routed to `35_Workflow_Governance` only for workflow/governance queries.
- Optional writing-time evidence expansion stops at `20_Paper_Memories`; `10_Project_Change_Log` is not loaded during writing retrieval.

## Query Results

### 4.3 interface wave SPH-FEM explosion welding figure rewrite new journal interfacial wave mechanism plastic strain jet

- Phase: `none`
- Selected limit: `8`
- Layers: `45_Supervision, 40_Final_Generalized_Rules, 50_Conflicts, 60_Limited_Rules, 30_Writing_Rules`
- Baseline: `17` files, `4830` tokens
- RAG: summaries `1049` + selected full `4411` = `5460` tokens
- Saved: `0` tokens (`0.0%`)
- Evidence decision: `not_expanded` | score `1` / threshold `3`
- Selected files:
  - `40_Final_Generalized_Rules/Paper framing should keep interface wave and intermetallic compound as dual mainlines.md` | `263` tokens
    - links out: `Paper framing should keep interface wave and intermetallic compound as dual mainlines, User decision - interface wave and intermetallic compound dual mainline`
    - links in: `none`
  - `30_Writing_Rules/Paper framing should keep interface wave and intermetallic compound as dual mainlines.md` | `213` tokens
    - links out: `User decision - interface wave and intermetallic compound dual mainline`
    - links in: `Paper framing should keep interface wave and intermetallic compound as dual mainlines`
  - `40_Final_Generalized_Rules/Abstract opening should state object-variable-effect.md` | `338` tokens
    - links out: `Abstract final rule - intermetallic layer thickness and distribution, Abstract opening should state object-variable-effect, Introduction numerical method naming and abstract abbreviation preference, Introduction revision aligned with mentor abstract dual mainline, Keyword selection rule - method object morphology mechanism process, Mentor feedback - Chinese expression grammar and academic style, Mentor feedback - abstract framing and priority rule, User decision - abstract opening compromise, User decision - interface wave and intermetallic compound dual mainline`
    - links in: `none`
  - `30_Writing_Rules/Abstract opening should state object-variable-effect.md` | `296` tokens
    - links out: `Abstract final rule - intermetallic layer thickness and distribution, Introduction numerical method naming and abstract abbreviation preference, Introduction revision aligned with mentor abstract dual mainline, Keyword selection rule - method object morphology mechanism process, Mentor feedback - Chinese expression grammar and academic style, Mentor feedback - abstract framing and priority rule, User decision - abstract opening compromise, User decision - interface wave and intermetallic compound dual mainline`
    - links in: `Abstract opening should state object-variable-effect`
  - `40_Final_Generalized_Rules/Method description should serve the research purpose.md` | `330` tokens
    - links out: `Abstract final rule - intermetallic layer thickness and distribution, Introduction numerical method naming and abstract abbreviation preference, Introduction polishing must preserve causal transition structures, Introduction revision aligned with mentor abstract dual mainline, Keyword selection rule - method object morphology mechanism process, Mentor feedback - abstract framing and priority rule, Method description should serve the research purpose, Paper memory export path convention, User decision - interface wave and intermetallic compound dual mainline`
    - links in: `none`
  - `30_Writing_Rules/Method description should serve the research purpose.md` | `288` tokens
    - links out: `Abstract final rule - intermetallic layer thickness and distribution, Introduction numerical method naming and abstract abbreviation preference, Introduction polishing must preserve causal transition structures, Introduction revision aligned with mentor abstract dual mainline, Keyword selection rule - method object morphology mechanism process, Mentor feedback - abstract framing and priority rule, Paper memory export path convention, User decision - interface wave and intermetallic compound dual mainline`
    - links in: `Method description should serve the research purpose`
  - `40_Final_Generalized_Rules/Reference upgrades must preserve sentence-level support.md` | `308` tokens
    - links out: `Abstract final rule - intermetallic layer thickness and distribution, Abstract rule - direct opening superseded version, Abstract rule - predict layer thickness and distribution, DOCX manuscript edits must distinguish partial drafts from full manuscript, Introduction numerical method naming and abstract abbreviation preference, Introduction revision - references and second paragraph structure, Paper memory export path convention, Reference upgrades must preserve sentence-level support`
    - links in: `none`
  - `30_Writing_Rules/Reference upgrades must preserve sentence-level support.md` | `265` tokens
    - links out: `Abstract final rule - intermetallic layer thickness and distribution, Abstract rule - direct opening superseded version, Abstract rule - predict layer thickness and distribution, DOCX manuscript edits must distinguish partial drafts from full manuscript, Introduction numerical method naming and abstract abbreviation preference, Introduction revision - references and second paragraph structure, Paper memory export path convention`
    - links in: `Reference upgrades must preserve sentence-level support`
  - `45_Supervision/2026-06-04 Abstract opening needs industry and problem background.md` | `738` tokens
    - links out: `Abstract opening should connect application context to core relation`
    - links in: `none`
  - `30_Writing_Rules/DOCX formula rewrites must verify math object structure.md` | `242` tokens
    - links out: `DOCX formula rewrite requires OMML structure check`
    - links in: `none`
  - `40_Final_Generalized_Rules/Literature review should progress through capability and limitation.md` | `345` tokens
    - links out: `DOCX manuscript edits must distinguish partial drafts from full manuscript, Introduction experimental literature requires method plus contribution, Introduction final paragraph should not copy abstract contribution wording, Introduction numerical method naming and abstract abbreviation preference, Introduction revision - references and second paragraph structure, Literature review should progress through capability and limitation, Same paragraph literature phrasing should avoid repeated templates, User decision - interface wave and intermetallic compound dual mainline`
    - links in: `none`
  - `30_Writing_Rules/Literature review should progress through capability and limitation.md` | `299` tokens
    - links out: `DOCX manuscript edits must distinguish partial drafts from full manuscript, Introduction experimental literature requires method plus contribution, Introduction final paragraph should not copy abstract contribution wording, Introduction numerical method naming and abstract abbreviation preference, Introduction revision - references and second paragraph structure, Same paragraph literature phrasing should avoid repeated templates, User decision - interface wave and intermetallic compound dual mainline`
    - links in: `Literature review should progress through capability and limitation`
  - `40_Final_Generalized_Rules/Abstract opening should connect application context to core relation.md` | `266` tokens
    - links out: `Abstract opening should connect application context to core relation, User decision - abstract opening compromise`
    - links in: `none`
  - `30_Writing_Rules/Abstract opening should connect application context to core relation.md` | `220` tokens
    - links out: `User decision - abstract opening compromise`
    - links in: `2026-06-04 Abstract opening needs industry and problem background, Abstract opening should connect application context to core relation`
