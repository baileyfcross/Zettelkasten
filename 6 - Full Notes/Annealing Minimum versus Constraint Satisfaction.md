2026-10-17 17:30

Status: #baby

Tags: [[Quantum Annealing and QUBO Programming]]

# Annealing Minimum versus Constraint Satisfaction

A quantum annealer always samples from an objective that has at least one minimum over its finite binary domain. It does not return a special “unsatisfiable” result merely because the encoded constraints conflict.

When every constraint can be met, the ground-state energy can be designed to certify a valid solution. When they cannot, the minimum is the least penalized compromise. A formulation must therefore track the energy or validity condition that separates a satisfying assignment from a best-effort assignment rather than interpreting every lowest sample as logically valid.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

