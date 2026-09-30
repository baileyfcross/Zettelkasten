2026-09-06 19:44

Status: #baby

Tags: [[Numerical Error and Conditioning]]

# Strict Diagonal Dominance

A square matrix is strictly diagonally dominant when, in every row, the absolute diagonal entry is greater than the sum of the absolute values of all other entries in that row.

This structural condition guarantees nonsingularity and supplies a useful sufficient condition for convergence of the [[Jacobi Method]] and [[Gauss-Seidel Method]]. It is sufficient, not necessary: some nondominant systems also converge.

The nonsingularity proof selects a component of a hypothetical null vector having maximal absolute value. The dominant row then forces the diagonal contribution to be strictly larger than all possible off-diagonal cancellation, a contradiction.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[linearalgebra.pdf]]
