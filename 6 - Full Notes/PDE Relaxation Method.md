2026-10-03 16:11

Status: #baby

Tags: [[Numerical PDE Methods]]

# PDE Relaxation Method

The relaxation method starts with trial values at the interior mesh points of an elliptic problem and evaluates how strongly each finite-difference equation is violated. Corrections are chosen to reduce the largest residuals and their effects on neighboring equations.

The process repeats until all residuals are negligible to the required accuracy. It combines the local simplicity of a finite-difference stencil with targeted corrections instead of solving the entire linear system in one direct calculation.

# References

[[numericalmethodsinengineeringandscience.pdf]]

