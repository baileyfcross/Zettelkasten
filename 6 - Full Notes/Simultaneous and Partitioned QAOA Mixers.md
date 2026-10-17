2026-10-17 17:30

Status: #baby

Tags: [[Constraint-Preserving QAOA]]

# Simultaneous and Partitioned QAOA Mixers

A simultaneous mixer implements $e^{-i\beta\sum_j H_j}$ for the complete mixing Hamiltonian. A partitioned mixer instead applies a product of local factors $e^{-i\beta H_j}$ in a chosen order, often grouping commuting odd, even, and wraparound couplings.

When the local terms do not commute, different orders give different unitaries and the product only approximates the simultaneous evolution at low order. Partitioning can reduce implementation depth or match connectivity, but ordering becomes part of the ansatz rather than a neutral compilation choice.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

