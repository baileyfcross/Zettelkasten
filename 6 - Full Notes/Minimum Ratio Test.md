2026-10-03 22:06

Status: #baby

Tags: [[Simplex Algorithms and Basis Structure]]

# Minimum Ratio Test

The minimum ratio test chooses which basic variable leaves during a primal simplex iteration. For rows with a positive coefficient in the entering column, the current right-hand side is divided by that coefficient, and the smallest nonnegative ratio identifies the limiting row.

The test preserves feasibility because no basic variable is allowed to fall below zero. A tied or zero minimum ratio can produce [[Linear Programming Degeneracy]], where a pivot changes the basis without a strict objective improvement.

# References

[[optimizationusinglinearprogramming.pdf]]

