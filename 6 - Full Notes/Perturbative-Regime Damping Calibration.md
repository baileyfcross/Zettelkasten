2026-10-15 10:35

Status: #baby

Tags: [[Linear-Rescaling Error Mitigation for VQE]]

# Perturbative-Regime Damping Calibration

Perturbative-regime damping calibration estimates a noisy circuit's multiplicative suppression where the Hamiltonian has a classically tractable limit, then transfers that factor to a harder parameter regime. The method assumes the damping is approximately independent of the Hamiltonian coupling that is varied between calibration and target problems.

For the mixed-field Ising benchmark, the authors fix $h_z=0.1$, average observed damping factors for $h_x=0.1$ through $0.5$, and use that average to correct the nonperturbative target at $h_x=1.5$. It predicts the target damping well on two IBM devices through roughly 25 ansatz layers, although it fails by 50 layers and does not reproduce the factor exactly.

The calibration requires separately optimizing and measuring circuits for several perturbative Hamiltonians. It therefore applies only after optimization and only when a useful perturbative regime exists. Its strong empirical performance is balanced by model-specificity and greater calibration overhead than [[Circuit-Depth Damping Extrapolation]].

# References

[[2021 - Experimental error mitigation using linear rescaling for variational quantum eigensolving with up to 20 qubits.pdf]]
