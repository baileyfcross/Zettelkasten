2026-10-14 17:27

Status: #baby

Tags: [[Unary-Encoded Quantum Neural Networks]]

# Orthogonal Matrix-to-Pyramid Compilation

Every special orthogonal matrix can be represented by the angles of a [[Quantum Pyramidal Circuit]]. The compilation procedure traverses selected matrix entries column by column and solves sequential trigonometric equations; the circuit has the same number of free angles as the matrix has degrees of freedom.

An orthogonal matrix with determinant $-1$ first factors into a determinant-$1$ matrix and a diagonal reflection. The first factor maps to the RBS pyramid, while a final Pauli-$Z$ gate on the last qubit supplies the reflection on the unary subspace. The result extends the construction from $SO(n)$ rotations to all of $O(n)$.

# References

[[2022 - Quantum Methods for Neural Networks and Application to Medical Image Classification.pdf]]
