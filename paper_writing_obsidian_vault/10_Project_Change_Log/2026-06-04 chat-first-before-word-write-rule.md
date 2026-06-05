---
title: 2026-06-04 chat first before Word write rule
created: 2026-06-04 21:08
tags:
  - docx
  - layer/evidence
  - user-confirmation
  - user-preference
  - workflow
---

# 2026-06-04 Chat First Before Word Write Rule

## User Instruction

The user added a new rule: for all content the user asks Codex to revise, Codex must first provide the revised content in the chat box. Only after the user confirms that the content is acceptable should Codex write it into the Word document.

## Rule Meaning

- Applies to manuscript text, paragraph rewrites, formula descriptions, section revisions, translations intended for the manuscript, and other user-requested content changes.
- Codex should not directly modify `manuscript.docx` or other Word files with newly drafted content before the user confirms the proposed text in chat.
- After confirmation, Codex may write the approved text into Word and then run normal DOCX verification.
- Pure formatting repairs, file inspection, extraction, or knowledge-base maintenance are outside this rule unless they also change manuscript content.

## Existing Related Rule

The closest previous governance rule was `DOCX edit scope must be verified before manuscript changes`, which checks whether the target Word file is the full manuscript or a partial draft. The new rule is different: it requires user content approval before Word insertion.
