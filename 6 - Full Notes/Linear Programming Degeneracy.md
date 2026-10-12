2026-10-03 22:06

Status: #baby

Tags: [[Simplex Algorithms and Basis Structure]]

# Linear Programming Degeneracy

Linear programming degeneracy occurs when a basic feasible solution has at least one basic variable equal to zero. It can arise from a tied limiting ratio and may cause successive simplex tableaus to represent the same extreme point.

Degeneracy does not by itself make a model infeasible or nonoptimal, but it can stall progress and, under unsuitable pivot choices, repeat bases. A small perturbation of right-hand-side values is one way to separate tied constraints while preserving the intended limiting solution.

# References

[[optimizationusinglinearprogramming.pdf]]

