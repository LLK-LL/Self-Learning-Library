---
title: DOCX terminology unification and Windows processing pitfalls
created: 2026-06-03
tags:
  - EDS
  - docx
  - layer/evidence
  - paper-memory
  - process-memory
  - terminology
  - windows-encoding
---

# DOCX terminology unification and Windows processing pitfalls

## Memory Content

When standardizing terminology in a Word manuscript, first scan the `.docx` with a structured API and confirm whether the requested term actually appears. In this round, `元素分析` did not appear, but one equivalent or adjacent expression, `EDS 测量`, appeared in paragraph 13 and was unified to `EDS分析获得`.

For `.docx` processing on this Windows workspace:

- Use `python-docx` rather than raw replacement inside the zipped Word XML package when a local paragraph/run edit is enough.
- Inspect runs around the target phrase before editing; in this case `EDS` and `测量` were split into adjacent runs.
- Save to a new `.docx` unless the user explicitly asks to overwrite.
- Reopen the output file and verify package validity, paragraph count, term counts, and special characters.
- In PowerShell, do not use Unix here-doc syntax such as `python - <<'PY'`.
- If `python` is not on PATH, use the Windows `py` launcher.
- When printing manuscript text containing non-GBK characters, reconfigure Python stdout to UTF-8.

## Applicability

Use this memory before future `.docx` manuscript operations, especially terminology unification, tracked local edits, and verification of Chinese academic text containing chemical formula formatting.
