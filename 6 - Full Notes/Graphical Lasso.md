2026-09-29 19:17

Status: #baby

Tags: [[High-Dimensional Graphical Models]]

# Graphical Lasso

Graphical Lasso estimates a Gaussian precision matrix by minimizing negative log-likelihood plus an $\ell_1$ penalty on off-diagonal entries. The diagonal is left unpenalized because marginal conditional variances are not expected to vanish.

The objective combines a convex log-determinant term with a sparsity penalty, producing a computable estimator even when the empirical covariance is singular. Zeros in the result define missing graph edges through [[Precision Matrix Conditional Independence]]. Performance still depends on structural conditions and tuning; a convex solution is not automatically an accurate recovered graph when $n\le p$.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
