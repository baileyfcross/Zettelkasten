2026-09-06 19:44

Status: #baby

Tags: [[Matrix Invertibility and Factorization]] · [[R Matrix Systems and Scientific Models]]

# Singular Matrix

A singular matrix is a [[Square Matrix]] with zero [[Determinant]]. It has no [[Matrix Inverse]] and does not have full [[Matrix Rank]].

For $Ax=0$, singularity permits nonzero solutions. In numerical methods it may also prevent a factorization step or triangular solve from producing a unique solution.

The student companion forms a singular two-equation coefficient matrix by making one row a scalar multiple of the other while leaving incompatible right-hand sides. The corresponding lines are parallel, providing a visual explanation for why R cannot return a unique inverse-based solution.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[rstudentcompanion.pdf]]
