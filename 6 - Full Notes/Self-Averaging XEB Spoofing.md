2026-10-17 03:33

Status: #baby

Tags: [[Random-Circuit Quantum Advantage Verification]]

# Self-Averaging XEB Spoofing

Self-averaging spoofing replaces each omitted cross-partition gate with maximal depolarizing noise, equivalently averaging over randomized single-qubit operations at the cut. Averaging suppresses instance-specific fluctuations while preserving a provably positive mean correlation with the ideal circuit for suitable random gate ensembles.

The modification makes [[Top-k XEB Amplification]] more reliable because the amplified score is less likely to be dominated by a few accidental bitstrings. Its price is mixed-state rather than pure-state simulation, although identities for fSim-like gates can propagate the depolarizing channel efficiently. The construction matters conceptually because it converts a heuristic partitioning attack into a lower-variance challenge to average-XEB hardness.

# References

[[2024 - Limitations of Linear Cross-Entropy as a Measure for Quantum Advantage.pdf]]

