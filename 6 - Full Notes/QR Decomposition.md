2026-09-06 19:44

Status: #baby

Tags: [[Least Squares Methods]] · [[Matrix Algebra for Statistical Models]]

# QR Decomposition

QR decomposition factors a matrix as $A=QR$, where $Q$ has orthonormal columns and $R$ is upper triangular.

For full-column-rank least squares, orthogonality preserves residual length and reduces the problem to $R\hat x=Q^Tb$, completed by [[Back Substitution]]. This avoids the potentially ill-conditioned product $A^TA$ in the [[Normal Equation]].

The source uses QR factorization to explain how R fits linear models more stably than an explicit inverse of $X^T X$. The factorization also reveals matrix rank, connecting numerical computation to whether model coefficients are uniquely estimable.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]
