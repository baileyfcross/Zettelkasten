2026-10-03 16:11

Status: #baby

Tags: [[Numerical Quadrature Methods]]

# Simpson Three-Eighths Rule

Simpson's three-eighths rule integrates a cubic interpolant over three equal subintervals. For one panel its weights are $1,3,3,1$ with the weighted sum multiplied by $3h/8$.

In a composite calculation, the number of subintervals must be divisible by three. Interior nodes whose indices are multiples of three receive weight two, while the other interior nodes receive weight three.

# References

[[numericalmethodsinengineeringandscience.pdf]]

