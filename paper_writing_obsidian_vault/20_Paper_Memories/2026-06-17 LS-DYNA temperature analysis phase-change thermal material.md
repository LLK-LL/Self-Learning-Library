---
title: LS-DYNA temperature analysis phase-change thermal material
created: 2026-06-17
tags:
  - LS-DYNA
  - SPH
  - explosive-welding
  - layer/evidence
  - phase-change
  - thermal-coupling
---

# LS-DYNA Temperature Analysis Phase-Change Thermal Material

## Context

The user asked why a Johnson-Cook melting parameter of 1878 K did not prevent the computed interface temperature from exceeding 3000 K in an SPH explosive-welding simulation, then asked how to realize temperature limiting or plateauing when full thermal calculation is enabled.

## Reusable Technical Conclusions

- In LS-DYNA Johnson-Cook material cards, the melting temperature is primarily a thermal-softening reference in the homologous-temperature term. It should not be treated as a solver-imposed upper bound on temperature.
- If full thermal calculation is enabled, the physically preferable way to suppress rapid temperature rise at melting is not hard temperature clipping, but phase-change/latent-heat treatment.
- `*MAT_THERMAL_ISOTROPIC_PHASE_CHANGE` (`T09` / `*MAT_T05` in some interfaces) can define temperature-dependent heat capacity and thermal conductivity through `T1-T8`, `C1-C8`, and `K1-K8`, plus phase-change parameters `SOLT`, `LIQT`, and `LH`.
- `SOLT` is the solidus temperature, `LIQT` is the liquidus temperature, and `LH` is latent heat. During the phase-change interval, latent heat is represented by an enhanced effective heat capacity, causing a temperature plateau or slower temperature rise.
- This method does not guarantee an absolute temperature cap. Once latent heat is consumed and heat generation continues, temperature may still exceed the liquidus temperature.
- Hard clipping such as `if T > Tmelt then T = Tmelt` generally requires a user material/user thermal subroutine or custom post-processing logic and breaks energy conservation unless the excess energy is accounted for elsewhere.

## Unit System Used In This Project Discussion

The user showed the LS-DYNA unit system:

```text
kg, mm, ms, kN, GPa, kN-mm
```

Useful conversions:

```text
specific heat C: J/(kg K) = kN-mm/(kg K), numerical value unchanged
latent heat LH: J/kg = kN-mm/kg, numerical value unchanged
thermal conductivity K: W/(m K) -> multiply by 1.0E-6
density TRO: kg/m3 -> multiply by 1.0E-9 = kg/mm3
temperature T: K, numerical value unchanged
```

## Engineering Tables Discussed

For TC4 / Ti-6Al-4V, an engineering T09 table was proposed:

```text
T1-T8  = 293, 600, 1000, 1400, 1878, 1933, 2200, 3000
C1-C8  = 526, 610, 700, 780, 820, 830, 850, 880
K1-K8  = 6.70E-6, 8.20E-6, 1.10E-5, 1.40E-5,
         1.65E-5, 1.70E-5, 1.80E-5, 2.00E-5
SOLT   = 1878
LIQT   = 1933
LH     = 3.65E5
TRO    = 4.43E-6
```

For Al6061, an engineering T09 table was proposed:

```text
T1-T8  = 293, 500, 700, 850, 900, 925, 1600, 3000
C1-C8  = 896, 960, 1050, 1120, 1160, 1180, 1180, 1180
K1-K8  = 1.67E-4, 1.80E-4, 1.90E-4, 2.00E-4,
         1.10E-4, 9.00E-5, 9.00E-5, 9.00E-5
SOLT   = 855
LIQT   = 925
LH     = 4.00E5
TRO    = 2.70E-6
```

High-temperature points above the liquidus, especially 3000 K for Al6061, are engineering extrapolation points for numerical robustness, not reliable physical liquid-alloy data. They should be described cautiously if used in manuscript text.

## Al6061 Conductivity Note

Al6061 thermal conductivity should not be assumed to monotonically decrease over all temperatures. In solid-state ranges it may rise, plateau, or vary weakly depending on temper and microstructure. The proposed drop after the melting interval represents the transition to a liquid/alloy high-temperature approximation and the increased scattering/loss of solid-lattice structure. For SPH explosive-welding sensitivity analysis, a smoother or higher post-melting conductivity plateau can be tested to avoid artificially amplifying interface hot spots.

## Source Pointers

- LS-DYNA heat transfer class notes for phase-change thermal material behavior and latent heat treatment.
- LS-DYNA keyword documentation for `*MAT_THERMAL_ISOTROPIC_PHASE_CHANGE` fields.
- AZoM and MatWeb for Ti-6Al-4V melting range and room-temperature thermal properties.
- MatWeb, NIST, and BISON/INL documentation for Al6061 thermal properties and temperature-dependent conductivity/specific-heat context.

