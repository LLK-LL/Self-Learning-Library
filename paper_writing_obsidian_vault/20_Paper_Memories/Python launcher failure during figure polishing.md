---
title: Python launcher failure during figure polishing
created: 2026-06-05 12:31
tags:
  - figure
  - layer/evidence
  - python
  - workflow
source: user_instruction
priority: user_high
---

# Python Launcher Failure During Figure Polishing

## Problem

During Python-based figure polishing, the Windows `py` launcher failed with:

`No installed Python found!`

This blocked both the local RAG command when invoked with `py` and matplotlib runtime checks, even though Python was installed on the machine.

## Diagnosis

`Get-Command` showed `py.exe` at `C:\Windows\py.exe`, but direct inspection found installed Python directories under:

- `<python-installation>`
- `<python-installation>`

Direct execution of Python 3.12 confirmed the usable runtime and plotting stack:

- Python `3.12.6`
- matplotlib `3.10.8`
- numpy `2.4.2`

## Resolution

For project figure tasks, if `py` reports that no Python is installed, call the real interpreter directly:

`<python-installation>\python.exe`

This path worked for local RAG and matplotlib rendering.

## Reusable Rule

When a figure workflow has already selected Python, do not switch to R merely because the `py` launcher is broken. First check direct Python interpreter paths, verify matplotlib/numpy availability, and continue with Python if the real interpreter works.

## Related Change Log

[[2026-06-05 welding-window-curve-polished-python]]

