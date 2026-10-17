2026-10-17 17:30

Status: #baby

Tags: [[Quantum Annealing and QUBO Programming]]

# Additive Constraint Objective

Ising and QUBO objective terms are additive. If several component penalties share a common minimizing assignment, their sum is minimized on the intersection of their minimum sets. This lets a large constraint system be assembled from reusable local building blocks.

For example, a chain of equality penalties can enforce $A=B=C=D$ by adding pairwise terms for $A=B$, $B=C$, and $C=D$. If the component minima have no common assignment, the summed objective still has a minimum, but it represents the least costly compromise rather than a fully satisfied solution.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

