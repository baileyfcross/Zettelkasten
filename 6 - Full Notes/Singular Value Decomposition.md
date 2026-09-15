2026-09-06 19:44

Status: #baby

Tags: [[Numerical Eigenvalue Methods]] · [[Distance Geometry and Dimension Reduction]]

# Singular Value Decomposition

Singular value decomposition factors a real matrix as $A=UDV^T$, where $U$ and $V$ are orthogonal and $D$ is diagonal or rectangular diagonal with nonnegative singular values.

Unlike eigenvalue decomposition, SVD applies to rectangular matrices. It exposes rank and conditioning and provides stable formulas for the [[Pseudoinverse]] and [[Least Squares Approximation]].

For high-dimensional data, the source orders the transformed directions by decreasing sum of squares. Retaining the leading directions creates a lower-dimensional approximation that preserves dominant variation and often preserves much of the pairwise distance among samples.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]
