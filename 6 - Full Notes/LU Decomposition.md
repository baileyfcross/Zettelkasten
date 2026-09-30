2026-09-06 19:44

Status: #baby

Tags: [[Matrix Invertibility and Factorization]]

# LU Decomposition

LU decomposition factors a matrix as $A=LU$, where $L$ is [[Lower Triangular Matrix|lower triangular]] and $U$ is [[Upper Triangular Matrix|upper triangular]]. A system $Ax=b$ is then solved through $Ly=b$ followed by $Ux=y$.

The factorization is especially useful when several right-hand sides share the same coefficient matrix. Pivoting may require a [[Permutation Matrix]], producing $PA=LU$.

LU records Gaussian elimination: the entries below the diagonal in $L$ store elimination multipliers, while $U$ is the resulting row-echelon coefficient matrix. Without row exchanges, nonzero leading principal pivots provide a standard sufficient condition for the factorization.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[linearalgebra.pdf]]
