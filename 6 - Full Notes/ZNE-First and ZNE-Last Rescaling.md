2026-10-15 10:35

Status: #baby

Tags: [[Linear-Rescaling Error Mitigation for VQE]]

# ZNE-First and ZNE-Last Rescaling

Linear rescaling and zero-noise extrapolation can be composed in two different orders. In the ZNE-first construction, the target circuit and its calibration circuit are each extrapolated to zero noise, after which the extrapolated target value is divided by the damping factor inferred from the extrapolated calibration value.

In the ZNE-last construction, each noise-scaled target measurement is first divided by the damping factor from the calibration circuit at that same noise scale. The sequence of corrected ratios is then extrapolated to zero noise. The two orders need not agree because fitting and division are nonlinear operations on finite-shot data.

The paper benchmarks both variants using the zero-angle calibration circuit from [[Single-Qubit-Gate Omission Calibration]]. Neither combination consistently surpasses the more specialized perturbative-regime or circuit-depth calibrations, and both inherit the instability described by [[Deep-Circuit ZNE Signal Collapse]].

# References

[[2021 - Experimental error mitigation using linear rescaling for variational quantum eigensolving with up to 20 qubits.pdf]]
