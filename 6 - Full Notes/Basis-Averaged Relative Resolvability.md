2026-10-15 10:25

Status: #baby

Tags: [[Error-Mitigation Trainability of Variational Quantum Algorithms]]

# Basis-Averaged Relative Resolvability

Pairwise [[Relative Resolvability of Mitigated Cost Values]] depends on selected parameters, ansatz, observable, and noise realization. Basis-averaged relative resolvability instead fixes a noisy-state spectrum and averages the squared separation from the noise fixed point over conjugations drawn from a unitary 2-design.

This construction asks whether mitigation generally restores distinguishability for states with the same eigenvalues rather than whether it helps one chosen landscape. It is physically motivated by the loss of purity under unital noise: states with a common spectrum share the same purity even though their eigenbases differ.

The average exposes protocol-level limits that a favorable pair of parameters can hide. In particular, it leads to purity-dependent bounds for [[Virtual Distillation Purity-Resolvability Bound]] and a related observable-basis average for zero-noise extrapolation. These are ensemble statements, not guarantees for every individual circuit.

# References

[[2021 - Can Error Mitigation Improve Trainability of Noisy Variational Quantum Algorithms.pdf]]
