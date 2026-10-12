2026-09-06 19:44

Status: #baby

Tags: [[Matrix Invertibility and Factorization]]

# Positive-Definite Matrix

A real symmetric matrix $A$ is positive definite when $x^TAx>0$ for every nonzero vector $x$. Its eigenvalues are positive.

Positive definiteness guarantees important numerical behavior: [[Cholesky Decomposition]] exists, the [[Conjugate Gradient Method]] has a suitable energy minimization interpretation, and a positive-definite [[Hessian Matrix]] identifies a strict local minimum.

For a real symmetric matrix, positive definiteness is equivalent to every eigenvalue being positive. It is also equivalent to the existence of an invertible factor $B$ with $A=B^TB$, which makes the quadratic form a squared Euclidean norm after a change of variables.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[linearalgebra.pdf]]
