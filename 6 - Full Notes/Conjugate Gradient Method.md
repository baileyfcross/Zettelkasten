2026-09-06 19:44

Status: #baby

Tags: [[Iterative Linear System Methods]]

# Conjugate Gradient Method

The conjugate gradient method solves a [[Positive-Definite Matrix|symmetric positive-definite]] system by searching along mutually $A$-orthogonal directions. Each step minimizes a quadratic energy associated with $Ax=b$.

Used iteratively, it is valuable for large [[Sparse Matrix|sparse]] systems. The residual determines the first direction and helps generate later conjugate directions and a stopping test.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

