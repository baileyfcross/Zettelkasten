2026-09-06 19:44

Status: #baby

Tags: [[Simplex Algorithms and Basis Structure]]

# Two-Phase Simplex Method

The two-phase simplex method first minimizes the sum of [[Artificial Variable|artificial variables]] to find a feasible basis. If the phase-one optimum is zero, phase two restores the original objective and continues simplex optimization.

Separating feasibility from optimization avoids choosing an arbitrary large penalty as required by the [[Big M Method]].

A positive phase-one optimum proves that the original constraints are infeasible; a zero value permits artificial columns to be removed before the original objective is restored.

# References

[[numericalmethodsinengineeringandscience.pdf]]

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[optimizationusinglinearprogramming.pdf]]
