2026-10-03 16:11

Status: #baby

Tags: [[Numerical PDE Methods]]

# Richardson Scheme

The Richardson scheme for the one-dimensional heat equation uses a centered time difference together with a centered spatial second difference. It relates the future level to both the present and preceding levels.

Although the stencil is symmetric, the scheme is unstable for the diffusion equation: errors can grow as time stepping continues. This motivates alternatives such as the [[Dufort-Frankel Method]] and [[Crank-Nicolson Method]].

# References

[[numericalmethodsinengineeringandscience.pdf]]

