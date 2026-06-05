---
title: Partial DOCX mistaken for full manuscript
created: 2026-06-03 21:20
tags:
  - docx
  - layer/evidence
  - no-regression
  - project-change-log
---

# Partial DOCX mistaken for full manuscript

## What Happened

After the introduction experimental-literature revision and reference renumbering, the user noticed that the abstract and the first introduction paragraph were not present in the output DOCX.

Inspection showed that `manuscript_intro_p2_p4_chinese_polished_causality_restored_terms_unified.docx` and the backup created before renumbering both had empty early paragraphs and started real manuscript content at the experimental-literature introduction paragraph. The file name also indicates it is an `intro_p2_p4` working file, not a full manuscript.

## Cause

The editing target was a partial introduction working draft containing introduction paragraphs 2-4 and references. It was incorrectly treated as the active manuscript output without explicitly warning that the abstract and introduction first paragraph were not included in that file.

## Fix

For future DOCX manuscript edits, first extract the early paragraphs and verify whether the file contains:

- abstract
- introduction first paragraph
- target paragraph or section
- reference list

If the file is a partial working draft, state this before editing and do not present the result as a complete manuscript. Locate or request the full manuscript before producing a complete merged DOCX.
