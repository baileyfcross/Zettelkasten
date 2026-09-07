2026-09-06 19:44

Status: #baby

Tags: [[Least Squares Methods]]

# Overdetermined Least Squares

Overdetermined least squares addresses $Ax=b$ when $A$ has more rows than columns and an exact solution may not exist. It chooses $\hat x$ that minimizes $\|b-Ax\|_2$.

Geometrically, $A\hat x$ is the closest point to $b$ in the column space of $A$, making the residual orthogonal to that space. The computation can use a [[Normal Equation]], [[QR Decomposition]], or SVD.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]
