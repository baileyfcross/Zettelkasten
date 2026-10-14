2026-10-03 16:11

Status: #baby

Tags: [[Numerical ODE Methods]]

# Finite Difference Boundary Value Method

The finite difference boundary-value method replaces derivatives in an ODE and its boundary conditions with finite-difference approximations at grid points. The differential equation becomes a linear system for the unknown interior values.

Centered differences usually give better accuracy than basic one-sided formulas. A smaller step improves truncation accuracy but increases the number of simultaneous equations, so the method couples discretization choices to the cost and conditioning of the linear solve.

# References

[[numericalmethodsinengineeringandscience.pdf]]

