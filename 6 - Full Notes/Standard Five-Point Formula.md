2026-10-03 16:11

Status: #baby

Tags: [[Numerical PDE Methods]]

# Standard Five-Point Formula

For the two-dimensional Laplace equation on a square mesh, the standard five-point formula is

$$u_{i,j}=\frac14(u_{i-1,j}+u_{i+1,j}+u_{i,j-1}+u_{i,j+1}).$$

It states that each interior value is the average of its four axial neighbors. Applied at every interior node, it turns the boundary-value problem into a linear system or an iterative [[Liebmann Method]] update.

# References

[[numericalmethodsinengineeringandscience.pdf]]

