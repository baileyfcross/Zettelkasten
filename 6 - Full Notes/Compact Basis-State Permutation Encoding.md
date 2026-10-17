2026-10-16 23:18

Status: #baby

Tags: [[Symmetry-Equivariant Variational Quantum Learning]]

# Compact Basis-State Permutation Encoding

A compact permutation-equivariant encoding assigns each feature $x_k$ to the projector $|k\rangle\langle k|$. The generated unitary places a feature-dependent phase on one computational-basis amplitude, while exchanging two features is represented by a unitary that swaps the associated basis states.

Because $n$ qubits provide $2^n$ basis states, this scheme can encode exponentially many features while retaining an explicit representation of their permutations. The qubit saving is not free: a basis-state phase is generally controlled on nearly every qubit and is therefore much harder to implement than the local rotations in [[Permutation-Equivariant Qubit Encoding]].

Using every basis state also leaves very few nontrivial trainable operators that commute with all feature permutations. The example exposes a general encoding tradeoff between register width, gate locality, and the size of the surviving equivariant model class.

# References

[[2022 - Exploiting symmetry in variational quantum machine learning.pdf]]

