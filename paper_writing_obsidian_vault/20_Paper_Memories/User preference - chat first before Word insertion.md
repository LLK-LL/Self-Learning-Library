---
title: User preference - chat first before Word insertion
created: 2026-06-04 21:08
tags:
  - docx
  - layer/evidence
  - user-confirmation
  - user-preference
  - workflow-governance
source: user_instruction
priority: user_high
---

# User Preference - Chat First Before Word Insertion

For all future manuscript-content changes requested by the user, Codex must first provide the revised content in the chat box and wait for the user's confirmation. Only after the user confirms that the proposed text is acceptable should Codex write it into a Word document.

This applies to:

- paragraph rewrites;
- section rewrites;
- formula-description rewrites;
- translated or polished text intended for the manuscript;
- any newly drafted content that would replace or enter `manuscript.docx` or another Word manuscript file.

Boundaries:

- It does not block non-content actions such as reading files, checking formatting, extracting text, running RAG, or recording knowledge-base rules.
- It does not require confirmation for purely mechanical formatting fixes unless those fixes alter manuscript wording.
- If the user explicitly says to write directly into Word without preview, that newer instruction controls for that task.

Operational rule: final Word insertion should happen only after the user has approved the chat version.

Evidence: [[2026-06-04 chat-first-before-word-write-rule]]
