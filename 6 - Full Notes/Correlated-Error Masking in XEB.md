2026-10-17 03:33

Status: #baby

Tags: [[Random-Circuit Quantum Advantage Verification]]

# Correlated-Error Masking in XEB

Multiple circuit errors do not always contribute independently to XEB. When their propagated light cones overlap, one error can mask or partly cancel the benchmark-visible effect of another even though the physical circuit has accumulated both deviations. The resulting correction depends on the relative spacetime locations of the errors, not just their count.

This makes clustered or deliberately placed faults qualitatively different from homogeneous stochastic noise. A benchmark calibrated under independent errors can substantially overstate fidelity when correlations change which deviations survive at the input or measurement boundary. [[Circuit-Partitioning XEB Spoofing]] exploits the same vulnerability deliberately by concentrating omitted gates along subsystem boundaries.

# References

[[2024 - Limitations of Linear Cross-Entropy as a Measure for Quantum Advantage.pdf]]

