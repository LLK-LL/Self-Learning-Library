---
title: Mentor R01 introduction revision logic and advantages
created: 2026-06-05 10:55
tags:
  - introduction
  - layer/evidence
  - mentor-feedback
  - source/mentor
source: mentor
source_priority: mentor_high
scope: introduction
status: active
---

# Mentor R01 Introduction Revision Logic And Advantages

## Memory

The mentor-revised `Manuscript-R01.docx` introduction changes the original manuscript introduction from a literature-first structure into an application-problem-method-closure structure.

Key mentor changes:

- The introduction begins with the lightweight armour application context, impact-resistance demand, lightweight requirement, and TC4/Al6061 material advantages before discussing experiments and literature.
- The first paragraph connects material advantages to explosive welding, interface-wave formation, high-temperature melting zones, Ti/Al intermetallic compounds, and the performance relevance of interface-wave morphology and intermetallic-compound thickness.
- Experimental literature is framed as useful for final interface morphology, elemental distribution, microstructure, melting/reaction-zone morphology, and mechanical properties, but limited for observing transient wave, melting-zone, and intermetallic-compound evolution.
- Numerical-method literature is organized by method capability and limitation: Lagrangian grid distortion, Eulerian boundary-tracking weakness, S-ALE limited thermo-plastic coupling, SPH high cost at high resolution and possible numerical oscillation.
- The final paragraph justifies SPH-FEM through complementary advantages, then closes with model capability, temperature-field and Al3Ti-thickness inference, experimental validation, and process-optimization value.

## Reusable Lesson

For this project's introduction, mentor-level logic should prioritize the dual mainline of interface-wave formation and intermetallic-compound thickness/scale prediction. The argument should make SPH-FEM necessary by first establishing the application problem and then showing why experiment alone and single numerical methods are insufficient.

## Evidence

- Source file: `Manuscript-R01.docx`
- Compared against: `manuscript.docx`
- Review file: `Manuscript-R01-introduction-review-tracked.docx`
- Analysis report: `non_word_workspace/mentor_intro_revision_analysis_20260605.md`
