2026-10-15 00:14

Status: #baby

Tags: [[Quantum Computing for High-Energy Physics]]

# QUBO Wilson Coefficient Fitting

An effective field theory summarizes the observable influence of higher-energy physics through operators multiplied by Wilson coefficients. Experimental inference estimates those coefficients and their correlations from measured observables, often in a parameter space large enough to make global optimization difficult.

A quantum fitting scheme discretizes candidate coefficient values and converts the mismatch between effective-theory predictions and data into a quadratic unconstrained binary optimization problem. The QUBO becomes an Ising-like Hamiltonian whose low-energy bit string represents a best-fit coefficient assignment, allowing a quantum annealer to perform the optimization. In the reported construction, the effective-theory predictions themselves are computed classically; the quantum device solves only the coefficient-fit relationship.

This boundary prevents overclaiming what is quantum about the method. Discretization resolution, parameter correlations, uncertainty intervals, and embedding overhead determine whether the fit is useful. A reduced parameter example can show that the mapping works without demonstrating that a quantum annealer improves a realistic Standard Model Effective Field Theory analysis. [[Parameterized Quantum Circuit Parton Distribution Fitting]] instead uses a circuit as the fitted functional representation.

# References

[[2023 - Quantum Computing for High-Energy Physics State of the Art and Challenges Summary of the QC4HEP Working Group.pdf]]
