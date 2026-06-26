---
title: PowerShell-fed DOCX generators must use ASCII-safe source plus Unicode escapes
created: 2026-06-05 18:58
tags:
  - docx
  - encoding
  - implementation
  - layer/evidence
  - powershell
  - unicode
  - word
source: implementation_debug
priority: high
---

# PowerShell-Fed DOCX Generators Must Use ASCII-Safe Source Plus Unicode Escapes

When a DOCX file is generated on Windows by piping Python source through PowerShell, literal non-ASCII symbols in the shell-fed script can be converted into `?` before Python runs. This can corrupt visible manuscript content such as `Grüneisen`, `ε`, `ε̇`, and `γ`, even when the document structure and Python logic are otherwise correct.

Safer approach:

1. prefer a saved local `.py` generator over an inline shell-fed script;
2. keep the generator source ASCII-safe when possible;
3. represent special symbols with explicit Unicode escapes or code points, such as `\u00fc`, `\u03b5`, `\u03b3`, and `\u0307`;
4. after generation, inspect `word/document.xml` to confirm the intended Unicode characters were written into the DOCX body.

Boundary:

- terminal extraction may still display `?` because of console rendering, so XML inspection is the decisive check;
- this rule addresses character corruption, not formula layout, OMML structure, or Word COM save-path issues.

Evidence:

- [[2026-06-05 johnson-cook-gruneisen-docx-unicode-garbled-fix]]
- [[2026-06-04 unicode-encoding-issue-during-omml-rebuild]]
