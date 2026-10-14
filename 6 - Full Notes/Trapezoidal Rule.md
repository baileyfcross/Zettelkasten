2026-10-03 16:11

Status: #baby

Tags: [[Numerical Quadrature Methods]]

# Trapezoidal Rule

The trapezoidal rule replaces the integrand on each subinterval by a straight line. For uniform spacing $h$,

$$\int_{x_0}^{x_n}f(x)\,dx\approx\frac h2\left[y_0+2\sum_{i=1}^{n-1}y_i+y_n\right].$$

It is the first-degree [[Newton-Cotes Formula]]. Its composite error is proportional to $h^2$ when the second derivative is bounded, and [[Romberg Integration]] improves it by canceling successive even-power error terms.

# References

[[numericalmethodsinengineeringandscience.pdf]]

