2026-10-03 16:11

Status: #baby

Tags: [[Numerical ODE Methods]]

# Euler Method

For $y'=f(x,y)$, Euler's method advances by the tangent at the current approximation:

$$y_{n+1}=y_n+h f(x_n,y_n).$$

It is the first-order Runge-Kutta method and has first-order global accuracy. Its simplicity makes it useful for illustration, but a large step can make the polygonal approximation drift far from the true solution and its stability region is limited.

# References

[[numericalmethodsinengineeringandscience.pdf]]

