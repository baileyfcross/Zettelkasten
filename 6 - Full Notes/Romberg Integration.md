2026-10-03 16:11

Status: #baby

Tags: [[Numerical Quadrature Methods]]

# Romberg Integration

Romberg integration repeatedly applies the composite [[Trapezoidal Rule]] with halved step sizes and combines the results by extrapolation. If $R_{k,1}$ is the trapezoidal estimate, higher columns use

$$R_{k,j}=R_{k,j-1}+\frac{R_{k,j-1}-R_{k-1,j-1}}{4^{j-1}-1}.$$

Each column cancels another leading even power of the step-size error. The triangular table provides increasingly accurate estimates while reusing previously evaluated nodes.

# References

[[numericalmethodsinengineeringandscience.pdf]]

