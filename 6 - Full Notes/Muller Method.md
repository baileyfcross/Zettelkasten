2026-10-03 16:11

Status: #baby

Tags: [[Numerical Root-Finding Methods]]

# Muller Method

Muller's method generalizes the [[Secant Method]] by fitting a quadratic through three recent points on $y=f(x)$. One root of that quadratic becomes the next approximation to a root of the original function.

Because a quadratic can have complex roots, the iteration can move naturally from real starting values to a complex root. It requires no derivative, but the quadratic formula must be evaluated with a sign choice that avoids subtractive cancellation.

# References

[[numericalmethodsinengineeringandscience.pdf]]

