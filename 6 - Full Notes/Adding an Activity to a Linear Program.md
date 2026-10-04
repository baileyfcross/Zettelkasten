2026-10-03 22:06

Status: #baby

Tags: [[Linear Programming Duality and Sensitivity]]

# Adding an Activity to a Linear Program

Adding an activity introduces a new decision variable, an objective coefficient, and a column describing that activity's consumption of every constrained resource. The existing solution remains feasible because the new variable can initially be zero.

Its reduced cost is computed with the current dual values. If the optimality condition remains satisfied, the activity is not attractive at current resource prices; otherwise it enters the basis and primal simplex finds a new optimum.

# References

[[optimizationusinglinearprogramming.pdf]]

