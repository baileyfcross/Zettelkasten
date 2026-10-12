2026-10-03 16:11

Status: #baby

Tags: [[Numerical Root-Finding Methods]]

# Rate of Convergence in Root Finding

The rate of convergence describes how quickly a sequence of root approximations approaches its limit. If the errors satisfy approximately $|e_{n+1}|=C|e_n|^p$, then $p$ is the order of convergence.

Linear convergence has $p=1$ and removes roughly a fixed fraction of the error per step. Higher order gives faster local improvement: [[Bisection Method]] is linear, the [[Secant Method]] has order about $1.6$ when it converges, and [[Newton Root-Finding Method]] is normally quadratic near a simple root.

# References

[[numericalmethodsinengineeringandscience.pdf]]

