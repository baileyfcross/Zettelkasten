2026-09-29 19:17

Status: #baby

Tags: [[Sparse and Structured Regression]]

# Nuclear Norm Regularization

Nuclear norm regularization penalizes the sum of a matrix's singular values. Because rank counts nonzero singular values, the nuclear norm is a convex surrogate for a rank penalty in much the same way that the $\ell_1$ norm relaxes a count of nonzero coefficients.

In multivariate regression, adding this penalty to squared Frobenius loss promotes a low-rank coefficient matrix and yields a convex problem. Its risk can approach rank-constrained estimation when the design is sufficiently well conditioned. Combining it with a row-group penalty targets [[Sparse Low-Rank Regression]], although convexity alone does not guarantee optimal adaptation to both structures.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
