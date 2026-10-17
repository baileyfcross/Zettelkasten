2026-10-16 23:18

Status: #baby

Tags: [[Symmetry-Equivariant Variational Quantum Learning]]

# Symmetry-Orbit Parameter Sharing in Quantum Circuits

When a symmetry permutes qubits or couplings, locations in the same symmetry orbit must receive the same trainable operation for the layer to be equivariant. Parameter sharing is therefore the circuit-level manifestation of replacing individual generators with their orbit averages.

On a tic-tac-toe grid with dihedral symmetry, corners form one qubit orbit, edges another, and the center a third. Single-qubit parameters are shared within each class, while entangling parameters are shared across symmetry-equivalent corner-edge, edge-center, and center-corner connections. Removing reflection symmetry splits directed connections that rotation alone does not identify.

This sharing reduces the free-parameter count while preserving the geometric distinctions the task actually contains. It is a concrete implementation of an [[Equivariant Quantum Gateset]], not merely a generic regularization rule.

# References

[[2022 - Exploiting symmetry in variational quantum machine learning.pdf]]

