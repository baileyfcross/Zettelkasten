2026-09-06 19:44

Status: #baby

Tags: [[Numerical Eigenvalue Methods]] · [[Distance Geometry and Dimension Reduction]]

# Singular Value Decomposition

Singular value decomposition factors a real matrix as $A=UDV^T$, where $U$ and $V$ are orthogonal and $D$ is diagonal or rectangular diagonal with nonnegative singular values.

Unlike eigenvalue decomposition, SVD applies to rectangular matrices. It exposes rank and conditioning and provides stable formulas for the [[Pseudoinverse]] and [[Least Squares Approximation]].

For high-dimensional data, the source orders the transformed directions by decreasing sum of squares. Retaining the leading directions creates a lower-dimensional approximation that preserves dominant variation and often preserves much of the pairwise distance among samples.

Truncating the decomposition after rank $r$ gives the closest rank-at-most-$r$ matrix in Frobenius norm, with approximation error equal to the sum of squared discarded singular values. In [[Low-Rank Multivariate Regression]], one SVD of the response projected onto the design space produces all rank-constrained candidate fits.

The nonzero singular values are the square roots of the nonzero eigenvalues of $A^TA$ and $AA^T$. Their corresponding right and left singular vectors describe the input directions and output directions through which the matrix acts as independent scalar stretches.

For a sparse user-item utility matrix, a truncated decomposition supplies lower-dimensional user and item coordinates that expose latent preference structure. Two users can align along a hidden direction even without rating the same items, allowing recommendation evidence to survive the absence of direct neighborhood overlap.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]

[[introductiontohigh-dimensionalstatistics.pdf]]

[[linearalgebra.pdf]]

[[recommendationengines.epub]]
