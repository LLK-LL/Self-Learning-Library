---
title: 2026-06-05 editable Word chart figure VML text fix
created: 2026-06-05 12:45
tags:
  - editable-chart
  - figure
  - image-related
  - layer/evidence
  - word
---

# 2026-06-05 Editable Word Chart Figure VML Text Fix

## Problem

The first editable Word version of the welding-window curve used a hand-written VML group with VML lines and VML text boxes. In Word, the lines, frame, and shaded region were visible, but title text, axis labels, tick labels, and legend labels did not render. Only the ordinary Word paragraph below the figure appeared.

## Cause

Word accepted the VML geometry but did not reliably render the manually written VML textbox layer inside the grouped shape. Visual verification of line objects alone was insufficient because VML line compatibility does not guarantee VML textbox compatibility.

## Fix

The editable Word output was rebuilt as a native Word chart package rather than a VML shape group:

- `word/document.xml` contains a DrawingML chart reference.
- `word/charts/chart1.xml` contains the chart title, axes, series, and legend.
- `word/embeddings/welding_window_curve_source_chart.xlsx` stores the editable source data.
- The generated file is `figures/welding_window_curve/welding_window_curve_editable_chart_word.docx`.
- The companion data file is `figures/welding_window_curve/welding_window_curve_editable_chart_source.xlsx`.

The old VML output remains as a record of the failed approach and should not be used as the editable Word figure.

## Verification

- The generated DOCX zip package passed `ZipFile.testzip()`.
- The package contains `word/charts/chart1.xml`.
- The package contains an embedded Excel workbook under `word/embeddings/`.
- `word/document.xml` contains `w:drawing` and no VML tags.
- Chart XML contains the expected title and legend labels.

