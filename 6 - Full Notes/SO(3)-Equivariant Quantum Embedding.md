2026-10-16 23:18

Status: #baby

Tags: [[Symmetry-Equivariant Variational Quantum Learning]]

# SO(3)-Equivariant Quantum Embedding

A three-dimensional vector $x=(x_1,x_2,x_3)$ can be embedded into one qubit as $U(x)=\exp[-i(x_1X+x_2Y+x_3Z)/2]$. Rotating $x$ in ordinary three-dimensional space corresponds to conjugating this unitary by the associated $SU(2)$ rotation of the Bloch sphere.

The embedding is therefore equivariant to $SO(3)$: each spatial rotation has a unitary representative that produces exactly the same transformation of the Pauli-vector generator. This works because the fundamental action of the Lie algebra $\mathfrak{so}(3)$ on the data matches the adjoint action of $\mathfrak{su}(2)$ on the Pauli operators.

The construction covers proper rotations but not spatial inversion on one qubit. [[O(3)-Equivariant Quantum Embedding]] adds the missing reflection with an ancillary qubit.

# References

[[2022 - Exploiting symmetry in variational quantum machine learning.pdf]]

