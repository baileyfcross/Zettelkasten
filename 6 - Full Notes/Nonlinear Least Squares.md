2026-09-06 19:44

Status: #baby

Tags: [[Least Squares Methods]] · [[R Probability Simulation and Curve Fitting]]

# Nonlinear Least Squares

Nonlinear least squares minimizes squared residuals when model parameters enter the prediction function nonlinearly. Its optimality equations are generally nonlinear and may have multiple solutions.

A practical strategy linearizes the model around a current estimate and iteratively solves for parameter corrections. The result depends on starting values and convergence behavior.

The student companion uses R's nonlinear fitting interface for scientific equations whose parameters do not enter as simple linear coefficients. Starting values are part of the computational specification, and the fitted curve must be compared with the data because a reported convergence message does not establish substantive adequacy.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[rstudentcompanion.pdf]]
