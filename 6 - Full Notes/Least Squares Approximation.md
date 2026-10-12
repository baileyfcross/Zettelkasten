2026-09-06 19:44

Status: #baby

Tags: [[Least Squares Methods]]

# Least Squares Approximation

Least squares approximation chooses model parameters that minimize the sum of squared residuals between observed values and model predictions.

Unlike [[Interpolation]], the fitted function need not pass through every data point. This makes the method suitable for experimental observations containing error and for [[Overdetermined Linear System|overdetermined systems]] with no exact solution.

In matrix form, minimizing $\|Ax-b\|^2$ asks for the point in the column space of $A$ closest to $b$. The residual at a minimizer is orthogonal to every column of $A$, producing the [[Normal Equation]].

# References

[[numericalmethodsinengineeringandscience.pdf]]

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[linearalgebra.pdf]]
