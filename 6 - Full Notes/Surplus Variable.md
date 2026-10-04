2026-09-06 19:44

Status: #baby

Tags: [[Simplex Algorithms and Basis Structure]]

# Surplus Variable

A surplus variable converts a greater-than-or-equal constraint into an equality by subtracting a nonnegative quantity: $a^Tx-s=b$.

The surplus measures how far the left side exceeds the required minimum. Because its column does not automatically provide an identity basis, an [[Artificial Variable]] may also be needed.

Its negative unit coefficient distinguishes a surplus from the positive unit coefficient of a [[Slack Variable]] and explains why it cannot normally supply the starting basis by itself.

# References

[[numericalmethodsinengineeringandscience.pdf]]

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[optimizationusinglinearprogramming.pdf]]
