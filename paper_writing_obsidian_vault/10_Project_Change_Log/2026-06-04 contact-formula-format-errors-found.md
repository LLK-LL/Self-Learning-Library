---
title: Contact formula format errors found during DOCX inspection
created: 2026-06-04 13:55
tags:
  - docx-formula
  - error-finding
  - layer/evidence
---

# Discovered Errors

During inspection of the SPH-FEM contact-equation region around Eqs. (41)-(44), several formatting and content errors were identified:

- Some Word formula objects contained damaged OMML characters, which appeared as placeholder boxes in Word.
- Subscripts and superscripts were flattened or lost in the contact stiffness, effective mass and boundary traction equations.
- Inline OMML variables remained inside explanatory prose paragraphs and appeared as stray variable strings at the end of paragraphs.
- Several explanatory sentences used present perfect tense, although the user requested only simple present and simple past.

# Affected Region

The main affected equations were the contact-force, penalty stiffness, effective contact mass and contact-traction balance equations near Eqs. (41)-(44).

# Action

The formulas should be rebuilt as clean Word OMML objects, and prose paragraphs should use plain body formatting unless a standalone display equation is intended.
