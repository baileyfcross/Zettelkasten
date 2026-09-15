2026-09-06 19:44

Status: #baby

Tags: [[Least Squares Methods]] · [[Matrix Algebra for Statistical Models]]

# Linear Least Squares

Linear least squares fits a line $y=a+bx$ by minimizing the [[Residual Sum of Squares]]. Setting the derivatives with respect to $a$ and $b$ to zero produces two normal equations.

Although the fitted model is a line, the method generalizes directly to several linear parameters by writing the observations as $Ax\approx b$ and solving the [[Normal Equation]].

The source applies least squares to outcome vector $Y$ and design matrix $X$, choosing coefficients that minimize the residual sum of squares. This formulation covers group comparisons, continuous predictors, polynomial terms, and interactions within the same matrix framework.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]
