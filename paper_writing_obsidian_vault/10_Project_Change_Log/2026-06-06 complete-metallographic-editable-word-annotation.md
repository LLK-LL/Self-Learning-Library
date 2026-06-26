---
title: 2026-06-06 complete-metallographic-editable-word-annotation
created: 2026-06-06
tags:
  - editable-figure
  - figure-annotation
  - layer/evidence
  - metallographic
  - word-shapes
---

# Complete Metallographic Editable Word Annotation

## Change

Generated an editable Word figure for `修复后的图片/完整金相.png` at:

- `outputs/editable_figures/complete_metallographic_wave_dimensions_editable_word_shapes.docx`

## Implementation

Reused and patched `tools/create_editable_metallographic_annotation.ps1` instead
of creating a new script. The script now accepts:

- `-SourceImage` to avoid accidentally selecting the wrong PNG;
- `-OutputName` to control the generated DOCX filename.

The generated figure keeps the metallographic image as the base picture and
adds editable Word shape annotations for wavelength dimensions, wave-height
dimensions, material labels, welding direction, feature labels, dashed boxes,
arrows, and scale-bar text.

## Verification

The output DOCX contains:

- embedded source image: `word/media/image1.png`;
- editable Word drawing elements: `v:shape`, `v:line`, `v:rect`, and
  `v:textbox`;
- expected labels including `228 μm`, `232 μm`, `233 μm`, `236 μm`,
  `252 μm`, `63 μm`, `74 μm`, `72 μm`, `Vortex structure`, `Microcrack`,
  `Voids`, `Experimental result`, `Explosive welding direction`, `TC4`,
  `Al6061`, and `2000 μm`.

## Reuse Note

This task reused the existing editable metallographic annotation script with a
small scoped modification because it already used Word COM shapes and matched
the requirement for editable Word-format annotations.
