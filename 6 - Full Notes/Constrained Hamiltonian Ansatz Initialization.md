2026-10-12 18:53

Status: #baby

Tags: [[Hamiltonian Variational Ansatz Trainability]]

# Constrained Hamiltonian Ansatz Initialization

Constrained HVA initialization samples nonnegative preliminary parameters within each ansatz block and normalizes them so that their sum equals a fixed budget T proportional to 1/N. The paper's experiments use T = pi/(2N), placing each block in the short-time regime suggested by the [[Inverse-Qubit Hamiltonian Ansatz Parameter Budget]].

For one- and two-dimensional Heisenberg-XYZ circuits, this procedure maintains order-one averaged squared gradients across the tested system sizes, including up to 24 qubits in one dimension and 28 qubits in two dimensions. Fully random parameters show exponential decay in several corresponding settings, while [[Small-Constant Hamiltonian Ansatz Initialization]] displays a size-dependent crossover.

The constraint can also be enforced during optimization by defining one parameter as the block budget minus the others and penalizing negative values. The numerical evidence supports the initialization strategy for the studied local models and observables; it does not replace the theorem's nonzero-commutator and locality assumptions or resolve noise-induced barren plateaus.

# References

[[2023 - Hamiltonian variational ansatz without barren plateaus.pdf]]
