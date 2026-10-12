2026-10-03 22:06

Status: #baby

Tags: [[Linear Programming Duality and Sensitivity]]

# Adding a Constraint to a Linear Program

Adding a constraint can only preserve or shrink a linear program's feasible region, so it cannot improve the objective of the current optimum. The existing solution is first substituted into the new restriction.

If it satisfies the restriction, the constraint is redundant at that solution and the optimum remains. If it violates the restriction, the constraint can be added to the final tableau; the objective condition is retained while feasibility is recovered with the [[Dual Simplex Method]].

# References

[[optimizationusinglinearprogramming.pdf]]

