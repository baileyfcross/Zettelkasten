2026-10-16 23:18

Status: #baby

Tags: [[Symmetry-Equivariant Variational Quantum Learning]]

# Equivariant Quantum Data Embedding

A quantum data embedding $U(x)$ is equivariant to a data symmetry $V_s$ when transforming the input is equivalent to conjugating the embedding by a unitary representation $U_s$ on the quantum Hilbert space:

$$U(V_s[x])=U_sU(x)U_s^\dagger.$$

This relation transports a known classical symmetry into the circuit. Without it, later trainable gates have no consistent Hilbert-space action with which to commute, so the symmetry cannot be enforced systematically throughout a re-uploading model.

The representation need not be unique. What matters is that the chosen encoding makes the diagram from data transformation to quantum conjugation commute. [[Permutation-Equivariant Qubit Encoding]] and [[SO(3)-Equivariant Quantum Embedding]] give discrete and continuous constructions.

# References

[[2022 - Exploiting symmetry in variational quantum machine learning.pdf]]

