2026-09-06 19:44

Status: #baby

Tags: [[Simplex Algorithms and Basis Structure]]

# Slack Variable

A slack variable converts a less-than-or-equal [[Linear Constraint]] into an equality by recording unused capacity. For $a^Tx\leq b$, adding $s\geq0$ gives $a^Tx+s=b$.

Slack variables often form the initial basis of a simplex tableau. A zero slack value means the associated constraint is binding.

Their unit columns make less-than resource constraints especially convenient starting rows for a canonical simplex basis.

# References

[[numericalmethodsinengineeringandscience.pdf]]

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[optimizationusinglinearprogramming.pdf]]
