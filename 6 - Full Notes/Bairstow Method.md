2026-10-03 16:11

Status: #baby

Tags: [[Numerical Root-Finding Methods]]

# Bairstow Method

The Lin-Bairstow method finds a quadratic factor $x^2+px+q$ of a real polynomial. Synthetic division expresses the remainder as $Rx+S$, and linearized corrections to $p$ and $q$ are repeatedly chosen to drive both $R$ and $S$ toward zero.

A converged quadratic produces a real pair or a complex-conjugate pair of roots. The factor can then be removed by [[Polynomial Deflation]], allowing the procedure to continue on the lower-degree quotient without using complex arithmetic during the iteration.

# References

[[numericalmethodsinengineeringandscience.pdf]]

