2026-10-03 16:11

Status: #baby

Tags: [[Numerical Root-Finding Methods]]

# Polynomial Deflation

Polynomial deflation removes a known factor after a root has been approximated. If $\alpha$ is a root of $P(x)$, synthetic division forms a lower-degree polynomial $Q(x)$ such that $P(x)=(x-\alpha)Q(x)$, apart from any residual caused by approximation.

The remaining roots are then found from $Q$. Deflation reduces the size of the problem, but error in $\alpha$ perturbs the deflated coefficients and can degrade later roots, so the extracted root should be refined before division.

# References

[[numericalmethodsinengineeringandscience.pdf]]

