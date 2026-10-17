2026-10-17 17:30

Status: #baby

Tags: [[Constraint-Preserving QAOA]]

# Controlled Independent-Set Mixer

For vertex $u$, an independent-set partial mixer applies an $X$ rotation to qubit $u$ only when all neighbor qubits are zero. It can therefore add or remove $u$ without ever creating an edge whose two endpoints are both selected.

The total mixer is an ordered product of these vertex-conditioned rotations. Neighboring partial mixers generally do not commute, so product order changes the unitary and can change performance. The construction makes graph adjacency part of the quantum transition rule rather than only part of a penalty Hamiltonian.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

