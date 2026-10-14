2026-10-03 16:11

Status: #baby

Tags: [[Numerical ODE Methods]]

# Taylor Series Method for ODEs

The Taylor series method advances an ODE solution by evaluating $y'$, $y''$, and higher derivatives from the differential equation, then substituting them into a truncated Taylor expansion around the current point.

It can be highly accurate when the derivatives are easy to obtain. Its main drawback is that repeated differentiation becomes cumbersome for complicated equations, so it is often used to generate starting values for multistep methods instead of as the main algorithm.

# References

[[numericalmethodsinengineeringandscience.pdf]]

