---
title: SPH-FEM energy equation staged derivation
created: 2026-06-04
tags:
  - formulas
  - layer/evidence
  - sph-fem
  - thermo-plastic-coupling
---

# Memory

For the SPH-FEM thermo-plastic coupling section, the energy equation should not be introduced only as a final pair of temperature update equations. The clearer manuscript logic is:

1. place the SPH particle energy equation in Section 3.1;
2. place the FEM summation/discrete energy equation in Section 3.2;
3. define the interface contact heat source in Section 3.3;
4. assemble the coupled SPH-FEM block energy equation in Section 3.3.

# Rationale

This sequence makes the numerical method easier to audit because the SPH particle contribution, FEM matrix contribution, and interface heat exchange are separated before being combined. It also makes the cancellation of conductive contact heat and the partition of frictional heat explicit.

# Evidence

- User request on 2026-06-04 asked to derive the energy equation separately in SPH and FEM, then combine them through the coupling algorithm.
- User correction on 2026-06-04 clarified that the SPH derivation must be written into Section 3.1, the FEM derivation must be written into Section 3.2, and the FEM energy equation should use the same Gaussian summation style as the FEM momentum equation.
- The corrected round moved the SPH energy equations to Section 3.1, moved the FEM energy equations to Section 3.2, and retained only contact-source assembly plus the coupled equation in Section 3.3.
