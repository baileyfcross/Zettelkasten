2026-10-12 17:40

Status: #baby

Tags: [[Variable-Structure Variational Quantum Circuits]]

# VAns Noise-Adaptive Circuit Depth

In the paper's noisy eight-qubit Ising VQE benchmark, VAns changes its retained circuit size as the simulated noise strength changes. Lower noise permits deeper circuits, whereas stronger noise makes additional gates more costly and drives the search toward shallower layouts, including a separable solution at the highest tested setting.

The simplified lambda noise model applies bit-flip errors to preparation and measurement, then depolarizing, phase-flip, and amplitude-damping channels after gates. Two-qubit depolarizing noise is set an order of magnitude above its single-qubit counterpart, while qubit-dependent calibration, idle noise, connectivity restrictions, and crosstalk are omitted.

Across 50 optimization repetitions per setting, VAns outperforms the tested one-, two-, and three-layer hardware-efficient circuits and shows lower relative variation around its best cost. This evidence is specific to the synthetic noise model and small system; it demonstrates adaptive resource selection, not hardware-validated noise resilience.

# References

[[2022 - A semi-agnostic ansatz with variable structure for quantum machine learning.pdf]]
