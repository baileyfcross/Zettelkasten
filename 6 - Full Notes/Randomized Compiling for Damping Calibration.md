2026-10-15 10:35

Status: #baby

Tags: [[Linear-Rescaling Error Mitigation for VQE]]

# Randomized Compiling for Damping Calibration

Randomized compiling replaces each CNOT by a randomly selected dressed CNOT that implements the same ideal operation. Averaging these equivalent realizations tailors coherent, circuit-dependent errors toward a stochastic Pauli or depolarizing description.

That noise tailoring supports damping-factor models because depolarizing-like errors more naturally produce an approximately uniform contraction of traceless observables. The experiment samples among 16 dressed versions of every CNOT when comparing mitigation techniques.

Randomized compiling is used for the post-optimization mitigation benchmarks but not for the unmitigated VQE training runs. Its role is therefore to stabilize the noise model used by calibration, not to explain the training convergence in [[Unmitigated SPSA VQE under Observable Damping]].

# References

[[2021 - Experimental error mitigation using linear rescaling for variational quantum eigensolving with up to 20 qubits.pdf]]
