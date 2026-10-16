2026-10-15 10:43

Status: #baby

Tags: [[Randomized Compiling and Zero-Noise Extrapolation]]

# Coherent-Error Response Linearization

Coherent gate errors can make an observable respond nonlinearly and state-dependently to increasing circuit noise. In the paper's H2 example, the expectation values of the Hamiltonian's 14 Pauli terms vary strongly nonlinearly as each CNOT is replaced by larger odd repetitions, because coherent amplitudes can accumulate quadratically rather than as independent faults.

Randomized compiling changes that response. Averaging Pauli-dressed implementations converts the coherent contribution into an effective stochastic Pauli channel, and the expectation values become approximately linear in the number of noisy CNOT applications.

This linearization is the mechanism behind the synergy: [[Identity-Insertion Noise Magnification]] produces meaningful extrapolation points only after noise tailoring makes their trend regular enough for zero-noise extrapolation. It explains why either method alone can remain inaccurate while their composition achieves [[RC-ZNE VQE Energy Error Reduction]].

# References

[[2022 - Synergetic quantum error mitigation by randomized compiling and zero-noise extrapolation for the variational quantum eigensolver.pdf]]
