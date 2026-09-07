2026-09-06 19:44

Status: #baby

Tags: [[Least Squares Methods]]

# Normal Equation

For a least squares problem $Ax\approx b$, the normal equation is $A^TA\hat x=A^Tb$. It expresses that the residual $b-A\hat x$ is orthogonal to every column of $A$.

If the columns of $A$ are linearly independent, the equation has the unique solution $(A^TA)^{-1}A^Tb$. Forming $A^TA$ can worsen conditioning, so [[QR Decomposition]] or [[Singular Value Decomposition]] may be more stable.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

