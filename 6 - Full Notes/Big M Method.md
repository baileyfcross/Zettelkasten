2026-09-06 19:44

Status: #baby

Tags: [[Simplex Algorithms and Basis Structure]]

# Big M Method

The Big M method assigns every [[Artificial Variable]] a very large objective penalty and then applies the [[Simplex Method]].

A feasible solution to the original model must leave all artificial variables at zero. A positive artificial variable in the final basis signals that the original constraints are infeasible.

Before simplex iterations, the objective row is made canonical by eliminating the large-penalty coefficients of any artificial variables initially in the basis.

# References

[[numericalmethodsinengineeringandscience.pdf]]

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[optimizationusinglinearprogramming.pdf]]
