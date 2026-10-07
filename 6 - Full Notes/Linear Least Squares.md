2026-09-06 19:44

Status: #baby

Tags: [[Least Squares Methods]] · [[Matrix Algebra for Statistical Models]] · [[R Matrix Systems and Scientific Models]] · [[R Probability Simulation and Curve Fitting]]

# Linear Least Squares

Linear least squares fits a line $y=a+bx$ by minimizing the [[Residual Sum of Squares]]. Setting the derivatives with respect to $a$ and $b$ to zero produces two normal equations.

Although the fitted model is a line, the method generalizes directly to several linear parameters by writing the observations as $Ax\approx b$ and solving the [[Normal Equation]].

The source applies least squares to outcome vector $Y$ and design matrix $X$, choosing coefficients that minimize the residual sum of squares. This formulation covers group comparisons, continuous predictors, polynomial terms, and interactions within the same matrix framework.

The student companion derives a fitted line from the normal equations and later extends the same squared-error criterion to quadratic and multiple-predictor models. R's matrix operations make the parameter calculation explicit, while the overlaid curve shows whether the chosen form follows the data.

Solving the normal equations squares the condition number of the design matrix. Orthogonalization with the [[Gram-Schmidt Process]] or a [[Singular Value Decomposition]] can obtain the least-squares solution without relying on an explicit inverse of $X^TX$.

# References

[[numericalmethodsinengineeringandscience.pdf]]

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]

[[rstudentcompanion.pdf]]

[[statisticalcomputingincplusplusandr.pdf]]
