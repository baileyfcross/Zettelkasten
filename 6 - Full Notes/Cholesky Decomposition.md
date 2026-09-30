2026-09-06 19:44

Status: #baby

Tags: [[Matrix Invertibility and Factorization]]

# Cholesky Decomposition

Cholesky decomposition factors a real [[Positive-Definite Matrix|symmetric positive-definite matrix]] as $A=LL^T$, where $L$ is lower triangular with positive diagonal entries.

The symmetry eliminates the need to store two unrelated triangular factors. Solving $Ax=b$ becomes the successive systems $Ly=b$ and $L^Tx=y$.

The positive diagonal convention makes the factor unique. Cholesky can also be viewed as a Gram-type factorization, since $x^TAx=\|L^Tx\|^2$ directly displays positive definiteness.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[linearalgebra.pdf]]
