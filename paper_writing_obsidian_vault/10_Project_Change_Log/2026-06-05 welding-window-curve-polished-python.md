---
title: 2026-06-05 welding window curve polished with Python
created: 2026-06-05 12:31
tags:
  - figure
  - layer/evidence
  - python
  - welding-window
---

# 2026-06-05 Welding Window Curve Polished With Python

## Task

The user asked to polish the provided `v_c-v_p` welding-window curve using the `nature-figure` workflow and selected Python as the plotting backend.

## Process

- Loaded the figure workflow contract and Python backend rules.
- Retrieved project-local writing/tooling context with lightweight RAG.
- Searched existing scripts before creating a helper script.
- Reused the publication export style from the existing matplotlib schematic script, but created a new narrow plotting script because no existing welding-window curve script was found.
- Exported editable/vector and high-resolution raster outputs:
  - `figures/welding_window_curve/welding_window_curve_polished.svg`
  - `figures/welding_window_curve/welding_window_curve_polished.pdf`
  - `figures/welding_window_curve/welding_window_curve_polished.tiff`
  - `figures/welding_window_curve/welding_window_curve_polished.png`

## Blocker And Resolution

The `py` launcher failed with `No installed Python found!`, even though Python installations were present. The workaround was to call the real Python 3.12 interpreter directly:

`<python-installation>\python.exe`

This preserved the selected Python-only figure backend and avoided switching to R.

## Script Reuse Decision

A new script was created at `figures/welding_window_curve/draw_welding_window_curve.py` because the project contained a reusable matplotlib export pattern but no existing script for the welding-window curve itself.

