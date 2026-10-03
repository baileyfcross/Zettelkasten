2026-10-03 16:11

Status: #baby

Tags: [[Numerical Root-Finding Methods]]

# Aitken Delta-Squared Acceleration

Aitken's delta-squared process accelerates a linearly convergent sequence $x_n$ by combining three consecutive values. With $\Delta x_n=x_{n+1}-x_n$, the transformed estimate is

$$\hat{x}_n=x_n-\frac{(\Delta x_n)^2}{\Delta^2x_n}.$$

Applied to [[Fixed-Point Iteration]], it attempts to estimate and remove the dominant geometric error. The transformation is unusable when the second difference is zero or so small that division amplifies numerical error.

# References

[[numericalmethodsinengineeringandscience.pdf]]

