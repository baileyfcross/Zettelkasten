2026-10-12 19:52

Status: #baby

Tags: [[Hierarchical Multigrid Variational Quantum Algorithms]]

# Discrete Laplacian Hamiltonian Encoding

A finite-difference discretization turns the [[Laplacian Operator]] into a tridiagonal matrix whose boundary rows depend on the selected boundary condition. Dirichlet boundaries produce diagonal entries of two with adjacent negative-one entries, periodic boundaries also couple the first and last coordinates, and zero-derivative Neumann boundaries change the two endpoint diagonal entries to one.

For a dimension that is a power of two, the paper represents the Dirichlet matrix with Pauli terms and a cyclic-shift unitary. The shift increments computational-basis indices modulo the register size, while an additional transformed term distinguishes the Dirichlet operator from its periodic counterpart. The commuting terms used in the simulation allow their expectation to be evaluated from one measurement setting per shot.

The periodic ground state is an equal superposition that can be prepared directly with Hadamard gates, so the paper uses the less trivial Dirichlet ground state for its [[Multigrid Dirichlet Laplacian VQE]] benchmark. This encoding is specific to the stated one-dimensional discretizations and does not by itself cover more complicated boundaries.

# References

[[2023 - Hierarchical Multigrid Ansatz for Variational Quantum Algorithms.pdf]]
