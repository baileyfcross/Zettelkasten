2026-10-03 16:11

Status: #baby

Tags: [[Numerical PDE Methods]]

# Poisson Equation Finite Difference Method

For $u_{xx}+u_{yy}=f(x,y)$ on a square mesh, centered differences give

$$u_{i-1,j}+u_{i+1,j}+u_{i,j-1}+u_{i,j+1}-4u_{i,j}=h^2 f_{i,j}.$$

This is the forced counterpart of the [[Laplace Equation Finite Difference Method]]. Applying it at every interior node and inserting the boundary values yields a sparse linear system for the approximate field.

# References

[[numericalmethodsinengineeringandscience.pdf]]

