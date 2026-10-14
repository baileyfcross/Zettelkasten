2026-10-03 16:11

Status: #baby

Tags: [[Interpolation Methods]]

# Cubic Spline Interpolation

Cubic spline interpolation fits a separate cubic polynomial on each interval between adjacent data points. At every interior knot, the neighboring pieces agree in value, first derivative, and second derivative.

The resulting piecewise curve is smooth without requiring one high-degree polynomial over the entire table. Boundary conditions determine the remaining freedom; a natural spline makes the endpoint second derivatives zero and continues linearly outside the fitted interval.

# References

[[numericalmethodsinengineeringandscience.pdf]]

