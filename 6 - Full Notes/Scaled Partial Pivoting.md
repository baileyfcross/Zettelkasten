2026-09-06 19:44

Status: #baby

Tags: [[Direct Linear System Solvers]]

# Scaled Partial Pivoting

Scaled partial pivoting compares potential pivots relative to the largest magnitude entry in each candidate row. It chooses the row with the largest ratio rather than the largest raw entry.

This protects [[Gaussian Elimination]] when rows have very different scales, because a moderately sized pivot may still be dangerously small compared with the other coefficients in its row.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

