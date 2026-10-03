2026-10-03 16:11

Status: #baby

Tags: [[Numerical PDE Methods]]

# Crank-Nicolson Method

The Crank-Nicolson method discretizes the heat equation by averaging the spatial second-difference operator between the current and next time levels. The result is an implicit system coupling neighboring unknowns on the new level.

Compared with the explicit [[Schmidt Method]], each time step requires solving simultaneous equations but gains second-order time accuracy and improved stability. Boundary values enter the first and last equations of the tridiagonal system.

# References

[[numericalmethodsinengineeringandscience.pdf]]

