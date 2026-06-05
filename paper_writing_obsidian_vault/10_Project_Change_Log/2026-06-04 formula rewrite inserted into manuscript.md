---
title: 2026-06-04 formula rewrite inserted into manuscript
created: 2026-06-04 12:35
tags:
  - docx
  - formula-rewrite
  - layer/evidence
---

# Change

Inserted an English theoretical formulation section into `manuscript.docx` before the reference list.

Source document: `Manuscript-R0319-Without Mark.docx`.

Target document: `manuscript.docx`.

Added content:

- explosion-welding window formulas
- Richter flyer-plate kinematics
- SPH approximation, continuity, momentum, and artificial viscosity
- FEM mass conservation and SPH-FEM contact penalty coupling
- thermo-plastic energy equation for heat calculation
- Johnson-Cook temperature-dependent flow stress relation

Additional references from the source manuscript were appended as `[32]` to `[45]` to support formula sources and related constitutive/numerical equations.

# No-Regression Notes

- The inserted section preserves the interface-wave and intermetallic-compound dual mainline by linking the thermo-plastic SPH-FEM formulation to transient temperature concentration and Ti-Al intermetallic-compound estimation.
- No numerical simulation result, material parameter, or experimental result was invented.
- The Word formula objects in the source manuscript were checked through `word/document.xml` because plain DOCX paragraph extraction flattened fractions, radicals, and integral limits.
