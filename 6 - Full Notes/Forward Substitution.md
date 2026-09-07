2026-09-06 19:44

Status: #baby

Tags: [[Direct Linear System Solvers]]

# Forward Substitution

Forward substitution solves a [[Lower Triangular Matrix|lower triangular]] system from the first equation downward. Each newly determined unknown is substituted into the remaining equations.

It is the first solve after [[LU Decomposition]]: one finds $y$ from $Ly=b$, then uses [[Back Substitution]] to find $x$ from $Ux=y$.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

