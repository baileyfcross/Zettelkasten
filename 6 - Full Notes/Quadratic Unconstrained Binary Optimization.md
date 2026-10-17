2026-10-17 17:30

Status: #baby

Tags: [[Quantum Annealing and QUBO Programming]]

# Quadratic Unconstrained Binary Optimization

A quadratic unconstrained binary optimization problem minimizes

$$
O(x)=\sum_i a_i x_i+\sum_{i<j}b_{ij}x_i x_j,
\qquad x_i\in\{0,1\},
$$

often written $x^TQx$. Linear coefficients occupy the diagonal of $Q$ because $x_i^2=x_i$ for binary variables, and pairwise coefficients occupy the off-diagonal entries.

“Unconstrained” means explicit constraints are not supplied separately. They are represented by penalty terms inside the objective, so invalid assignments receive higher energy than the feasible optima. This makes formulation quality part of the algorithm.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

