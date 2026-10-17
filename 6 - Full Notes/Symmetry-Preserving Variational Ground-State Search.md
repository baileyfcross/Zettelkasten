2026-10-16 23:18

Status: #baby

Tags: [[Symmetry-Equivariant Variational Quantum Learning]]

# Symmetry-Preserving Variational Ground-State Search

A symmetry-preserving ground-state ansatz begins in the target Hamiltonian's symmetry sector and uses only gates that commute with the corresponding representation. The circuit then explores a smaller portion of Hilbert space without leaving the sector known to contain the ground state.

For the transverse-field Ising model, a positive-parity initial state and the standard QAOA generators preserve the global spin-flip symmetry. For the Heisenberg model, a product of singlets starts in the zero-total-spin sector, and twirling anisotropic pair interactions yields isotropic exchange generators of the same form used in a [[Hamiltonian Variational Ansatz]].

The restriction often reduced optimization iterations in the paper's simulations, but shallow equivariant circuits sometimes reached worse energies than more expressive non-equivariant circuits. Correct sector selection and sufficient depth are therefore prerequisites, not consequences, of symmetry preservation.

# References

[[2022 - Exploiting symmetry in variational quantum machine learning.pdf]]

