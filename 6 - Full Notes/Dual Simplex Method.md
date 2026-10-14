2026-10-03 22:06

Status: #baby

Tags: [[Linear Programming Duality and Sensitivity]]

# Dual Simplex Method

The dual simplex method starts from a basis that satisfies the primal optimality condition but violates primal feasibility. It pivots from one dual-feasible basis to another while repairing negative basic values, stopping when the primal basis also becomes feasible.

Unlike primal simplex, it chooses a leaving row before selecting the entering column. This reversal is useful after a new constraint or changed right-hand side disrupts feasibility without destroying the established objective-row condition.

# References

[[optimizationusinglinearprogramming.pdf]]

