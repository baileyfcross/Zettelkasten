2026-10-16 23:18

Status: #baby

Tags: [[Symmetry-Equivariant Variational Quantum Learning]]

# O(3)-Equivariant Quantum Embedding

An $SO(3)$-equivariant one-qubit embedding can be extended to the full orthogonal group by using two qubits and the generator $(x_1X+x_2Y+x_3Z)\otimes X$. Spatial rotations still act on the first qubit, while conjugating the second qubit by $Z$ changes $X$ to $-X$ and therefore sends $x$ to $-x$.

Rotations together with this inversion generate all of $O(3)$, including reflections through planes through the origin. The extra qubit is necessary in this construction because the one-qubit $SU(2)$ action is already fully used to represent proper rotations.

This is a concrete instance of the broader [[Lie-Algebra Criterion for Equivariant Quantum Embeddings]]: adding Hilbert-space dimension can create a representation unavailable in the smaller register.

# References

[[2022 - Exploiting symmetry in variational quantum machine learning.pdf]]

