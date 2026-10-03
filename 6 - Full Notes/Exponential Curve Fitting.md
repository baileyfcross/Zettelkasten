2026-10-03 16:11

Status: #baby

Tags: [[Least Squares Methods]]

# Exponential Curve Fitting

To fit $y=ae^{bx}$ with positive observations, take logarithms to obtain $\log y=\log a+(b\log e)x$. A straight-line fit in $(x,\log y)$ then estimates the transformed intercept and slope.

Exponentiating the intercept recovers $a$, and rescaling the slope recovers $b$. Because the residuals are minimized after the logarithmic transformation, the procedure emphasizes relative rather than equal absolute errors in the original $y$ values.

# References

[[numericalmethodsinengineeringandscience.pdf]]

