---
title: Editable Word figures need native charts not unverified VML textboxes
created: 2026-06-05 12:45
tags:
  - editable-chart
  - figure
  - image-related
  - layer/evidence
  - word
source: user_correction
priority: user_high
---

# Editable Word Figures Need Native Charts Not Unverified VML Textboxes

## User Correction

The user opened the generated editable Word figure and found that the curve, frame, and color line samples appeared, but all title, axis, tick, and legend text from the VML figure layer was missing.

## Lesson

For Word-editable scientific figures, do not treat a hand-written VML grouped shape as reliable merely because the line objects render. VML textboxes can fail while VML lines still appear, producing a figure with curves but no labels.

## Correct Workflow

For curve plots that must remain editable in Word:

1. Prefer a native Word chart with embedded Excel data.
2. Generate or preserve the source `.xlsx` data table.
3. In the DOCX package, use a DrawingML chart reference from `word/document.xml`.
4. Put chart semantics in `word/charts/chart1.xml`, including title, axes, legend labels, and series styles.
5. Embed the editable workbook under `word/embeddings/`.
6. Verify the package structure, not only the existence of a `.docx` file.
7. If Office COM is unavailable, manually writing OOXML chart parts is safer than manually writing VML textboxes.
8. If VML or shape textboxes are ever used, visually verify text rendering in Word before delivery.

## Regression Risk

A Word screenshot showing curves without labels means the geometry layer rendered but the text layer failed. The correct response is to switch to a native chart or verified Word textbox structure, not to tweak line coordinates.

## Related Change Log

[[2026-06-05 editable-word-chart-figure-vml-text-fix]]

