2026-10-15 10:43

Status: #baby

Tags: [[Randomized Compiling and Zero-Noise Extrapolation]]

# Finite-Shot RC-ZNE Robustness

The RC-ZNE improvement is not limited to exact state-vector expectation values. When the H2 Hamiltonian is decomposed into 14 Pauli terms and each term is estimated through simulated finite-shot sampling, combined randomized compiling and zero-noise extrapolation still reduces the coherent-noise energy error across the tested molecular configurations.

This test inserts two distinct sampling layers: shots estimate each Pauli expectation, and a finite circuit ensemble estimates the randomized-compiling average. Both feed uncertainty into the extrapolated objective and therefore into the classical optimization loop.

Persistence under simulated sampling supports the method's operational relevance, but the paper uses the simplest strategy of measuring every Pauli term separately and does not optimize measurement grouping or shot allocation. The result should therefore be read alongside [[Finite-Randomization Precision Scaling]] and [[Error-Mitigation Variance Cost]], not as a claim of low measurement overhead.

# References

[[2022 - Synergetic quantum error mitigation by randomized compiling and zero-noise extrapolation for the variational quantum eigensolver.pdf]]
