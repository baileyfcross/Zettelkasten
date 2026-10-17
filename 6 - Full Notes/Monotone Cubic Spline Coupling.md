2026-10-16 23:00

Status: #baby

Tags: [[Quantum Invertible Generative Models]]

# Monotone Cubic Spline Coupling

A monotone cubic spline coupling block replaces the elementwise linear map of an [[Affine Coupling Block]] with a piecewise cubic transformation. A conditioning subnet predicts the knot geometry and boundary slopes for the transformed variables while the other half of the input remains unchanged.

Constraining every segment to be monotone keeps the piecewise function invertible. The unchanged conditioning half also preserves the triangular-Jacobian argument used by [[Classical INN Coupling Architecture]].

Spline couplings require more computation but provide greater expressivity per parameter. The paper therefore uses them for its classical INN baselines when comparing model capacity with a quantum invertible network.

# References

[[2023 - Generative Invertible Quantum Neural Networks.pdf]]

