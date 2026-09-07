2026-09-06 19:44

Status: #baby

Tags: [[Linear Programming Methods]]

# Artificial Variable

An artificial variable is temporarily added to a constraint that lacks an obvious starting basic variable, especially an equality or greater-than-or-equal constraint.

It does not represent part of the original model and must be driven to zero. The [[Big M Method]] penalizes it in the objective, while the [[Two-Phase Simplex Method]] removes it through a separate feasibility phase.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

