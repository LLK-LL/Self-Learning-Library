---
title: Word COM should save professional formula DOCX through ASCII temp path
created: 2026-06-04 22:48
tags:
  - docx
  - docx-formula
  - implementation
  - layer/evidence
  - windows
source: implementation_debug
priority: medium
---

# Word COM Should Save Professional Formula DOCX Through ASCII Temp Path

When Word COM is used to create or professionalize formulas in this project, saving directly to the project path can fail or time out because the workspace path contains Chinese characters. During the English professional reactive Navier-Stokes attempt, direct `SaveAs` failed and direct `SaveAs2` to the project path timed out.

The safer route is:

1. generate and professionalize the formulas in Word;
2. save the DOCX to a short ASCII temporary path, such as `C:\Users\Administrator\Desktop\*.tmp.docx`;
3. close Word cleanly;
4. move the saved file into the project directory;
5. run the full post-BuildUp XML audit.

Boundary: this avoids save-path failures only. It does not replace formula layout and symbol checks.

Evidence: [[2026-06-04 english-professional-formula-generation-debug]]
