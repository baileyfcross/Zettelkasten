2026-10-15 10:35

Status: #baby

Tags: [[Linear-Rescaling Error Mitigation for VQE]] · [[Randomized Compiling and Zero-Noise Extrapolation]]

# Randomized Compiling for Damping Calibration

Randomized compiling replaces each CNOT by a randomly selected dressed CNOT that implements the same ideal operation. Averaging these equivalent realizations tailors coherent, circuit-dependent errors toward a stochastic Pauli or depolarizing description.

That noise tailoring supports damping-factor models because depolarizing-like errors more naturally produce an approximately uniform contraction of traceless observables. The experiment samples among 16 dressed versions of every CNOT when comparing mitigation techniques.

Randomized compiling is used for the post-optimization mitigation benchmarks but not for the unmitigated VQE training runs. Its role is therefore to stabilize the noise model used by calibration, not to explain the training convergence in [[Unmitigated SPSA VQE under Observable Damping]].

The VQE synergy study gives a cycle-level construction of the same mechanism. Random Pauli operations are inserted before noisy CNOT cycles, compensating Paulis are placed after them, and those easy operations are absorbed into neighboring single-qubit layers so the ideal circuit is unchanged. The paper applies this construction to both the original and noise-magnified circuits in [[RC-ZNE Circuit Evaluation Workflow]], using either 20 randomized compilations or an exact Pauli-channel average.

# References

[[2021 - Experimental error mitigation using linear rescaling for variational quantum eigensolving with up to 20 qubits.pdf]]

[[2022 - Synergetic quantum error mitigation by randomized compiling and zero-noise extrapolation for the variational quantum eigensolver.pdf]]
