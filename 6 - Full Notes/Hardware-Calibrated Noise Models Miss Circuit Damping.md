2026-10-15 10:35

Status: #baby

Tags: [[Linear-Rescaling Error Mitigation for VQE]]

# Hardware-Calibrated Noise Models Miss Circuit Damping

Two seemingly direct predictions from device calibration fail to reproduce the observed depth-dependent damping. Multiplying the reported fidelities of all gates in an observable's backward light cone predicts too much suppression for deep circuits on both tested devices.

A Qiskit Aer model using calibration-derived local depolarizing channels, thermal relaxation, and readout errors makes the opposite error and predicts too little suppression. Although this simulation is already too costly to scale, greater computational detail does not make its damping estimate accurate in the benchmark.

The disagreement shows that per-gate calibration metrics do not compose into a reliable circuit-level observable model. Empirical calibration with circuits matched to the target structure, as in [[Circuit-Depth Damping Extrapolation]], can capture effects missed by either independent-fidelity multiplication or a standard local-noise simulator.

# References

[[2021 - Experimental error mitigation using linear rescaling for variational quantum eigensolving with up to 20 qubits.pdf]]
