2026-10-03 16:11

Status: #baby

Tags: [[Numerical ODE Methods]]

# ODE Method Stability

An ODE method is stable when perturbations introduced by rounding, starting data, or an earlier step remain bounded in a way that follows the exact solution's behavior. Conditional stability restricts the step size; unconditional stability does not.

For the test equation $y'=\lambda y$, [[Euler Method]] multiplies each step by $1+h\lambda$ and is stable when $|1+h\lambda|<1$. Reducing $h$ lowers truncation error only until accumulated round-off begins to dominate.

# References

[[numericalmethodsinengineeringandscience.pdf]]

