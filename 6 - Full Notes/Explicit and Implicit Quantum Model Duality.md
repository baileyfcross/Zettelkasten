2026-10-16 17:27

Status: #baby

Tags: [[Quantum Chebyshev Modeling]]

# Explicit and Implicit Quantum Model Duality

An explicit quantum model receives a chosen value $x$ through a feature map and returns a scalar after repeated circuit evaluation. An implicit quantum model instead treats $x$ as a measurement outcome, so one circuit execution draws a sample from the Born distribution over basis states.

These views coincide when the feature map sends the zero state to an orthonormal state $|x\rangle$ and the readout is the corresponding zero-state projector. The same probability $p_\theta(x)$ can then be evaluated pointwise through the explicit overlap or sampled from a state prepared by the inverse adjustable circuit. The explicit form supports differentiation with respect to $x$, while the implicit form supports direct [[Distribution Sampling|sampling]]. The [[Quantum Chebyshev Transform]] supplies this duality for the nonuniform Chebyshev grid.

# References

[[2023 - Quantum Chebyshev Transform Mapping Embedding Learning and Sampling Distributions.pdf]]
