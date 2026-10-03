2026-10-03 16:11

Status: #baby

Tags: [[Numerical Root-Finding Methods]]

# Secant Method

The secant method approximates a function by the line through its two most recent iterates and uses that line's zero as the next estimate:

$$x_{n+1}=x_n-f(x_n)\frac{x_n-x_{n-1}}{f(x_n)-f(x_{n-1})}.$$

Unlike the [[Method of False Position]], it does not preserve a sign-changing bracket. It avoids the derivative required by [[Newton Root-Finding Method]] and converges with order about $1.6$ when successful, but it can fail if two function values coincide or the iterates leave the root's neighborhood.

# References

[[numericalmethodsinengineeringandscience.pdf]]

