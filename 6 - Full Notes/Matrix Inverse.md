2026-09-06 19:44

Status: #baby

Tags: [[Matrix and Vector Computation]]

# Matrix Inverse

An inverse of a square matrix $A$ is a matrix $A^{-1}$ satisfying $AA^{-1}=A^{-1}A=I$. It exists only when $A$ is a [[Nonsingular Matrix]], equivalently when its [[Determinant]] is nonzero.

For a system $Ax=b$, multiplication by the inverse gives $x=A^{-1}b$. In computation, a direct solver or [[LU Decomposition]] is usually preferable to explicitly forming the inverse.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

