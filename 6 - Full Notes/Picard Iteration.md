2026-10-03 16:11

Status: #baby

Tags: [[Numerical ODE Methods]]

# Picard Iteration

Picard iteration rewrites an initial-value problem $y'=f(x,y)$, $y(x_0)=y_0$, as the integral equation

$$y(x)=y_0+\int_{x_0}^{x}f(t,y(t))\,dt.$$

Starting with a simple approximation, each new function is obtained by inserting the preceding one under the integral. The method has major theoretical value and can yield a local series, but repeated symbolic integrations restrict its practical use.

# References

[[numericalmethodsinengineeringandscience.pdf]]

