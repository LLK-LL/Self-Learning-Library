---
title: Theory text overlap check against reference
created: 2026-06-04
tags:
  - layer/evidence
  - reference-check
  - text-overlap
---

# Change

Compared the explanatory text in the theory/formula section of `manuscript.docx` against the corresponding Section 3 text in `Manuscript-R0319-Without Mark.docx`.

# Method

- Compared theory-section body text only.
- New manuscript scope: XML paragraph indices `35-87`.
- Reference manuscript scope: XML paragraph indices `42-123`.
- Excluded formula tables, headings, figure captions/labels, and references.
- Saved reports to `process_files_20260604/theory_text_overlap_report.json` and `process_files_20260604/theory_text_overlap_report.md`.

# Result

- New body paragraphs compared: 46.
- Reference body paragraphs compared: 39.
- Mean best paragraph similarity: 0.447.
- Median best paragraph similarity: 0.413.
- Very high paragraph matches >= 0.80: 0.
- High paragraph matches 0.65-0.80: 3.
- Medium paragraph matches 0.50-0.65: 8.
- Low paragraph matches < 0.50: 35.
- Section-level 5-word shingle overlap: 2.26% of new manuscript shingles.

# Interpretation

The theory-section explanatory text does not show high overall textual repetition with the reference manuscript. Local similarity remains in a few method-description sentences around the SPH continuity equation and FEM momentum-equation explanation.
