2026-10-03 16:11

Status: #baby

Tags: [[Numerical Root-Finding Methods]]

# Multiple Root

A number $\alpha$ is a root of multiplicity $m$ when a polynomial contains the factor $(x-\alpha)^m$ but not $(x-\alpha)^{m+1}$. Equivalently, the function and its first $m-1$ derivatives vanish at $\alpha$, while the $m$th derivative does not.

Multiplicity changes numerical behavior. A repeated root need not produce a sign change, and ordinary [[Newton Root-Finding Method]] loses its usual quadratic convergence. If $m$ is known, multiplying the Newton correction by $m$ restores the faster local rate.

# References

[[numericalmethodsinengineeringandscience.pdf]]

