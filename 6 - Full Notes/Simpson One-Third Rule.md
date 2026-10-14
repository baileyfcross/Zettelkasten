2026-10-03 16:11

Status: #baby

Tags: [[Numerical Quadrature Methods]]

# Simpson One-Third Rule

Simpson's one-third rule integrates a quadratic interpolant through each pair of adjacent subintervals. On a uniform grid with an even number of subintervals, the weights follow the pattern $1,4,2,4,\ldots,2,4,1$ and the sum is multiplied by $h/3$.

The composite rule has error of order $h^4$ for a sufficiently smooth integrand. Requiring an even number of equal subintervals is part of the rule, not an optional implementation detail.

# References

[[numericalmethodsinengineeringandscience.pdf]]

