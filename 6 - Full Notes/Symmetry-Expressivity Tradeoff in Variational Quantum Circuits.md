2026-10-16 23:18

Status: #baby

Tags: [[Symmetry-Equivariant Variational Quantum Learning]]

# Symmetry-Expressivity Tradeoff in Variational Quantum Circuits

Enforcing symmetry restricts a variational circuit to transformations compatible with a selected representation. This reduces parameter count and focuses search on a relevant subspace, but it also removes states and functions the unconstrained circuit could express.

For supervised learning, that restriction can improve generalization because outputs that violate a known label symmetry are undesirable and may constitute [[Overfitting]]. For ground-state search, there is no analogous reward for matching a symmetry if a lower-energy approximation is available, and a shallow restricted ansatz can perform worse simply because it cannot reach the target accurately.

The paper's Ising and Heisenberg experiments show the depth dependence directly: non-equivariant ansatze can have lower energy at small depth, while sufficiently deep equivariant ansatze often converge faster and eventually match or outperform them. [[Partial Symmetry Enforcement in Variational Quantum Circuits]] offers ways to tune the restriction.

# References

[[2022 - Exploiting symmetry in variational quantum machine learning.pdf]]

