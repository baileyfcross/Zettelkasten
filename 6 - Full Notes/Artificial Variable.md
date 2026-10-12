2026-09-06 19:44

Status: #baby

Tags: [[Simplex Algorithms and Basis Structure]]

# Artificial Variable

An artificial variable is temporarily added to a constraint that lacks an obvious starting basic variable, especially an equality or greater-than-or-equal constraint.

It does not represent part of the original model and must be driven to zero. The [[Big M Method]] penalizes it in the objective, while the [[Two-Phase Simplex Method]] removes it through a separate feasibility phase.

Because its purpose is only to create an identity-basis column, a positive artificial variable remaining in the final basis means the original constraints have no feasible solution.

# References

[[numericalmethodsinengineeringandscience.pdf]]

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[optimizationusinglinearprogramming.pdf]]
