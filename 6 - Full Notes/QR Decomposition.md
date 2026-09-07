2026-09-06 19:44

Status: #baby

Tags: [[Least Squares Methods]]

# QR Decomposition

QR decomposition factors a matrix as $A=QR$, where $Q$ has orthonormal columns and $R$ is upper triangular.

For full-column-rank least squares, orthogonality preserves residual length and reduces the problem to $R\hat x=Q^Tb$, completed by [[Back Substitution]]. This avoids the potentially ill-conditioned product $A^TA$ in the [[Normal Equation]].

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]
