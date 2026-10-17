2026-10-16 23:00

Status: #baby

Tags: [[Quantum Invertible Generative Models]]

# Parameter-Shift QINN Jacobian

A QINN can evaluate input derivatives of expectation-valued outputs with parameter-shift rules analogous to those used for circuit-parameter gradients. Repeating the shifted circuit evaluations for every input-output pair yields the full [[Jacobian Matrix]], from which the [[Jacobian Determinant]] needed for likelihood training can be computed.

This differs from a classical coupling-based INN, whose architecture is designed to expose the determinant efficiently but does not generally make every Jacobian entry cheap. Full-matrix access could support analyses beyond density estimation, including selected latent directions and data-manifold geometry.

The paper presents this access as an architectural opportunity. Its collider experiment is simulated and does not benchmark the shot count, noise sensitivity, or scaling cost of estimating a full Jacobian on hardware.

# References

[[2023 - Generative Invertible Quantum Neural Networks.pdf]]

