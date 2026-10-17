2026-10-17 17:30

Status: #baby

Tags: [[Constraint-Preserving QAOA]]

# Feasible-Subspace QAOA Mixer

A feasible-subspace mixer preserves the span of valid computational-basis assignments. Starting from a feasible state, every alternating layer therefore assigns zero amplitude to configurations that violate hard constraints.

Preservation is not sufficient by itself. The mixer must also provide transitions that connect the relevant feasible states, or the algorithm can remain trapped in one disconnected component. Mixer design thus encodes both a conservation law and a neighborhood structure for the combinatorial search.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

