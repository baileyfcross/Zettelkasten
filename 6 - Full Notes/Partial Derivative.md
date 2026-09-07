2026-09-06 00:13

Status: #baby

Tags: [[Optimization and Differentiation]]

# Partial Derivative

A partial derivative measures how a function of several variables changes with respect to one variable while the others are held constant. It isolates the local effect of that variable on the output.

For a neural network, the variables include its many weights and biases and the output of interest is the [[Loss Function|loss]]. Collecting the partial derivatives for all parameters produces the [[Gradient]].

Second partial derivatives describe how these first-order rates change. Arranging every second and mixed partial derivative into a square array produces the [[Hessian Matrix]], which supports curvature tests and Newton-type optimization.

# References

[[algorithms.epub]]

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]
