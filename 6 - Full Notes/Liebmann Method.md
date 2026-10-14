2026-10-03 16:11

Status: #baby

Tags: [[Numerical PDE Methods]]

# Liebmann Method

The Liebmann method solves the finite-difference equations for an elliptic boundary-value problem by Gauss-Seidel iteration. Each interior node is replaced in sequence by the value prescribed by its five-point equation, using newly updated neighbors immediately.

Iterations continue until the nodal changes are sufficiently small. Because the procedure is iterative, a poor starting grid can still improve, and relaxation can accelerate convergence when ordinary updates are slow.

# References

[[numericalmethodsinengineeringandscience.pdf]]

