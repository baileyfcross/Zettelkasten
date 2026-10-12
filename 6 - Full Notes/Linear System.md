2026-09-06 19:44

Status: #baby

Tags: [[Linear System Structure]] · [[Matrix Algebra for Statistical Models]] · [[R Matrix Systems and Scientific Models]]

# Linear System

A linear system is a collection of linear equations in common unknowns. It can be written compactly as $Ax=b$, using a [[Coefficient Matrix]] $A$, an unknown vector $x$, and a right-hand-side vector $b$.

Depending on rank and dimensions, a system may have one solution, no solution, or infinitely many solutions. Numerical methods exploit matrix structure to solve it efficiently and accurately.

The source introduces matrix algebra through simultaneous scalar equations and then returns to the same structure when solving least-squares normal equations. Whether the coefficient matrix has independent columns determines whether the fitted parameter vector is uniquely identifiable.

The student companion translates simultaneous equations into $Ax=b$, solves them in R, and checks the result against the original equations. Real examples use the same representation for prediction and scientific mixture calculations, showing why the matrix form scales better than hand substitution.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]

[[rstudentcompanion.pdf]]
