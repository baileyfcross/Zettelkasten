2026-10-14 17:27

Status: #baby

Tags: [[Unary-Encoded Quantum Neural Networks]]

# Quadratic-Time Exact-Orthogonality Training

An $n$-dimensional [[Quantum Pyramidal Circuit]] contains $n(n-1)/2$ trainable rotations. Because [[RBS Angle-Space Backpropagation]] computes each local angle gradient with constant work, a complete classical weight-update step costs $O(n^2)$ while the represented matrix remains exactly orthogonal.

Earlier strict orthogonal-network updates on the Stiefel manifold require matrix products and a retraction costing $O(n^3)$. Singular-value-bounding methods also use an $O(n^3)$ decomposition and only restore approximate orthogonality. The angle parameterization therefore matches ordinary dense-layer backpropagation asymptotically while enforcing the structural constraint by construction.

# References

[[2022 - Quantum Methods for Neural Networks and Application to Medical Image Classification.pdf]]
