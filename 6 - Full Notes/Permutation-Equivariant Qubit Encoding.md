2026-10-16 23:18

Status: #baby

Tags: [[Symmetry-Equivariant Variational Quantum Learning]]

# Permutation-Equivariant Qubit Encoding

A direct way to encode permutation symmetry is to assign one feature to one qubit and encode each value with the same type of local rotation. For $d$ features, $R_Z(x_1)\otimes\cdots\otimes R_Z(x_d)$ turns a feature transposition into the corresponding qubit SWAP, thereby representing the [[Permutation Group]] on the Hilbert space.

The construction also supports coordinate sign flips: conjugating the affected $Z$ rotation with Pauli $X$ reverses its angle. Feature permutations and independent sign flips can therefore be combined into a larger semidirect-product symmetry.

Local rotations are shallow and transparent but require roughly one qubit per feature. Higher-order monomials can be included equivariantly only as complete symmetry orbits—for example, every permuted pair product needed by the selected group—so the number of encoded terms can grow quickly.

# References

[[2022 - Exploiting symmetry in variational quantum machine learning.pdf]]

