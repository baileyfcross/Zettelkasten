2026-09-06 19:44

Status: #baby

Tags: [[Linear System Structure]] · [[R Matrix Systems and Scientific Models]]

# Coefficient Matrix

The coefficient matrix of a [[Linear System]] contains the multipliers of the unknown variables. In $Ax=b$, it is the matrix $A$.

Its size, rank, sparsity, conditioning, and special structure determine which solving methods are appropriate. Appending the right-hand side forms the [[Augmented Matrix]].

The student companion builds the coefficient matrix in R from the multipliers written in a simultaneous-equation system. Keeping the unknown order consistent between columns and the solution vector is essential because the solver preserves position, not the informal variable names in the original equations.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[rstudentcompanion.pdf]]
