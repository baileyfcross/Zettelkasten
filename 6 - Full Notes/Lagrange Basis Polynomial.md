2026-09-06 19:44

Status: #baby

Tags: [[Interpolation Methods]]

# Lagrange Basis Polynomial

A Lagrange basis polynomial for node $x_i$ is $L_i(x)=\prod_{k\ne i}(x-x_k)/(x_i-x_k)$. It equals one at $x_i$ and zero at every other interpolation node.

These selector properties make the weighted sum in [[Lagrange Interpolation]] reproduce every supplied function value while remaining a polynomial of the required degree.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

