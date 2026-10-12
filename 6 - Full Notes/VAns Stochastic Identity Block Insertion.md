2026-10-12 17:40

Status: #baby

Tags: [[Variable-Structure Variational Quantum Circuits]]

# VAns Stochastic Identity Block Insertion

The VAns insertion step expands a circuit by sampling a block from the [[VAns Identity-Compiling Gate Dictionary]] and placing it at identity parameters. Different runs can therefore explore different regions of circuit-architecture space without suffering an immediate discontinuity in the objective when a block is added.

The paper samples dictionary sequences uniformly but biases the placement of two-qubit gates toward qubit pairs that are unconnected or have shared relatively few entangling gates. This heuristic spreads entanglement rather than repeatedly deepening an already dense part of the circuit.

The insertion operation itself is treated as constant-time with respect to qubit count and current circuit depth. Its proposals may still make the circuit larger, so every insertion is followed by [[VAns Informed Circuit Simplification]] before the new structure is evaluated and accepted.

# References

[[2022 - A semi-agnostic ansatz with variable structure for quantum machine learning.pdf]]
