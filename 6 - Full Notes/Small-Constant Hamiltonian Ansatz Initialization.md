2026-10-12 18:53

Status: #baby

Tags: [[Hamiltonian Variational Ansatz Trainability]]

# Small-Constant Hamiltonian Ansatz Initialization

Small-constant HVA initialization draws every parameter independently from a fixed interval from zero to epsilon, with epsilon independent of the qubit count. This differs from [[Constrained Hamiltonian Ansatz Initialization]], which normalizes an entire block to an explicit inverse-qubit budget.

In the paper's one-dimensional Heisenberg-XYZ experiments, gradients initially decay exponentially with system size but later enter a slower regime beyond a crossover size. Sweeping epsilon suggests that the boundary between these behaviors grows approximately with log N for the two-local circuit studied, which the authors relate heuristically to the depth at which a local random circuit becomes design-like.

This second trainable-looking regime is empirical and less general than the constrained theorem. The paper leaves open whether the same logarithmic relation holds for higher-locality Hamiltonians or higher-dimensional lattices. Small constants therefore provide a useful comparison and possible heuristic, not the rigorous protection supplied by the [[Inverse-Qubit Hamiltonian Ansatz Parameter Budget]].

# References

[[2023 - Hamiltonian variational ansatz without barren plateaus.pdf]]
