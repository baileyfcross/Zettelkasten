2026-10-03 16:11

Status: #baby

Tags: [[Numerical PDE Methods]]

# Finite Difference Approximation of Partial Derivatives

Partial derivatives on a [[Finite Difference Grid]] are approximated by differences along the appropriate coordinate direction. For example,

$$u_{xx}(x_i,y_j)\approx\frac{u_{i-1,j}-2u_{i,j}+u_{i+1,j}}{h^2}.$$

Replacing every derivative in a PDE and its boundary conditions creates algebraic equations for nodal values. Centered formulas commonly have an $O(h^2)$ spatial truncation error on a uniform mesh.

# References

[[numericalmethodsinengineeringandscience.pdf]]

