2026-10-15 10:43

Status: #baby

Tags: [[Randomized Compiling and Zero-Noise Extrapolation]]

# RC-ZNE VQE Energy Error Reduction

Combining randomized compiling with zero-noise extrapolation reduces coherent-noise energy errors in simulated molecular VQE by roughly one to two orders of magnitude. The effect appears for H2 and LiH dissociation calculations using UCC-SD ansatze and persists across over-rotation, local $XI$ and $IZ$ rotation, and coherent-crosstalk error models.

Randomized compiling alone reduces the worst coherent behavior but leaves a bias, while zero-noise extrapolation alone is applied to a nonlinear noise response and can substantially misestimate the energy. Their combination succeeds because [[Coherent-Error Response Linearization]] makes the amplified-noise data more suitable for extrapolation.

The result is numerical evidence rather than a hardware guarantee. It assumes stationary errors, emphasizes noisy entangling gates, and evaluates small molecules; [[Single-Qubit Noise Tolerance of RC-ZNE]] and [[Mixed Coherent and Relaxation Noise Mitigation]] test only selected departures from those assumptions.

# References

[[2022 - Synergetic quantum error mitigation by randomized compiling and zero-noise extrapolation for the variational quantum eigensolver.pdf]]
