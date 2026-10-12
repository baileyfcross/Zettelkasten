2026-09-06 19:44

Status: #baby

Tags: [[Least Squares Methods]]

# Pseudoinverse

The pseudoinverse generalizes matrix inversion to rectangular or rank-deficient settings. For a full-column-rank matrix, $A^+=(A^TA)^{-1}A^T$, and the least squares solution is $\hat x=A^+b$.

[[Singular Value Decomposition]] extends the construction by reciprocating nonzero singular values. For a nonsingular square matrix, the pseudoinverse equals the ordinary [[Matrix Inverse]].

The products $AA^+$ and $A^+A$ are orthogonal projectors onto the column and row spaces. This lets rank-constrained regression express a coefficient solution through the projected response even when the design is rectangular or rank deficient.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[introductiontohigh-dimensionalstatistics.pdf]]
