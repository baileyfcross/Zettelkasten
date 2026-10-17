2026-10-16 23:18

Status: #baby

Tags: [[Symmetry-Equivariant Variational Quantum Learning]]

# Invariant Boundary Conditions for Quantum Learning Models

Equivariant circuit layers do not by themselves guarantee an invariant scalar prediction. The initial state must satisfy $U_s|\psi_0\rangle=|\psi_0\rangle$, and the readout observable must satisfy $U_sOU_s^\dagger=O$ for every symmetry element.

With those endpoint conditions, an equivariant circuit maps a transformed input state to $U_s|\psi(x)\rangle$. The group unitaries then cancel on both sides of the observable in the expectation value, proving that the output is unchanged.

The same commutation equation has different roles for a trainable unitary and an observable. Conjugation by an invariant trainable unitary defines an equivariant channel on states, whereas an invariant observable is itself the fixed object used at readout. Together they close the construction of an [[Invariant Quantum Data Re-Uploading Model]].

# References

[[2022 - Exploiting symmetry in variational quantum machine learning.pdf]]

