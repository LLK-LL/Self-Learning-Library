---
title: Johnson-Cook Gruneisen DOCX unicode garbled fix
created: 2026-06-05 18:58
tags:
  - docx
  - encoding
  - layer/evidence
  - unicode
  - word
source: implementation_debug
priority: medium
---

# Johnson-Cook Gruneisen DOCX Unicode Garbled Fix

The standalone Word file `Johnson_Cook_Gruneisen_variable_explanations.docx` showed visible `?` characters in places where `Grüneisen`, `ε`, `ε̇`, and `γ` should have appeared.

Root cause:

- the document was generated from a Python script piped through PowerShell;
- literal non-ASCII characters in the shell-fed script were degraded by the local Windows console/code-page path before Python executed the source;
- the corrupted characters were then written into `word/document.xml`, so the DOCX itself contained `?` rather than valid Unicode text.

Fix applied:

1. verified the corruption by reading `word/document.xml` directly rather than trusting terminal rendering;
2. created `tools/create_johnson_cook_gruneisen_variable_explanations_docx.py` as a reusable local generator;
3. wrote the script in ASCII-safe source form and used explicit Unicode escape/code-point strings for `ü`, `ε`, `γ`, and the combining dot in `ε̇`;
4. regenerated `Johnson_Cook_Gruneisen_variable_explanations.docx`;
5. rechecked the XML to confirm the intended Unicode characters were present and the remaining `?` characters existed only in the XML declaration.

Takeaway:

- for Word/DOCX generation on Windows, literal Greek or math symbols must not be passed through PowerShell here-strings or pipe-fed Python source when the shell path can touch the local code page first;
- if a document looks garbled, inspect `word/document.xml` and search for literal `?` in the body text to distinguish real corruption from terminal display artifacts.
