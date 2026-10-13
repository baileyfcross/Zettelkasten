2026-10-12 19:52

Status: #baby

Tags: [[Hierarchical Multigrid Variational Quantum Algorithms]]

# Variational Quantum Problem Hierarchy

A variational quantum problem hierarchy represents one target as a sequence of smaller Hamiltonians or cost functions whose sizes increase toward the original instance. A multigrid optimizer solves each level and uses its circuit parameters to initialize the next, so the relationship between consecutive levels determines whether transferred information remains useful.

The paper defines different hierarchies for different domains. Discrete Dirichlet Laplacians increase the resolution encoded by the qubit register. MaxCut instances add one graph vertex and its incident edges at a time. Maximum Exact k-SAT instances add a variable and admit only clauses whose variables are all present at that level.

There is no universal refinement rule. Node order, variable order, interpolation choice, seed size, and the number of qubits added per level can change both the cost and the quality of the transferred solution. The paper uses simple generation orderings as a proof of concept and leaves more sophisticated hierarchy design open.

# References

[[2023 - Hierarchical Multigrid Ansatz for Variational Quantum Algorithms.pdf]]
