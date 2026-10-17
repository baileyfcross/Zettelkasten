2026-10-17 17:30

Status: #baby

Tags: [[Constraint-Preserving QAOA]]

# XY Mixer for One-Hot Constraints

An XY mixer uses pairwise generators $X_iX_j+Y_iY_j$ to exchange a single excitation between qubits. Because it rotates only within the $\{|01\rangle,|10\rangle\}$ subspace, it preserves total Hamming weight.

Applied inside each vertex's color register, the mixer moves the one in a one-hot assignment from one color to another without producing zero-color or multiple-color states. It therefore incorporates the coloring constraint into the dynamics instead of adding a penalty to the objective.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

