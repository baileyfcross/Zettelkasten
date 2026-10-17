2026-10-17 17:30

Status: #baby

Tags: [[Quantum Annealing and QUBO Programming]]

# Circuit Satisfiability QUBO Decomposition

A Boolean circuit can be converted to a QUBO by assigning variables to its inputs and intermediate wires, then adding one gate-consistency penalty for every relation. A final penalty forces the circuit output to true.

For a circuit built from NOT, OR, and AND gates, the complete objective is the sum of the corresponding local QUBOs. A zero- or minimum-penalty assignment then specifies inputs and internal wires that are mutually consistent and satisfy the requested output. Ancillary wire variables trade additional qubits for a quadratic local formulation.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

