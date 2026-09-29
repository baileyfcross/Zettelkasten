2026-09-29 19:17

Status: #baby

Tags: [[Sparse and Structured Regression]]

# Fused Lasso

Fused Lasso penalizes the absolute differences between neighboring coefficients. It promotes variation sparsity: most adjacent coefficients become equal, leaving only a small number of jumps.

This structure is useful for ordered variables, segmentation, and piecewise-constant signals. Reparameterizing the coefficients by their increments turns the problem into an ordinary [[Lasso Estimator]] with a transformed design. The ordering is therefore substantive, not cosmetic; applying the penalty to arbitrarily ordered features would impose unsupported adjacency relationships.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
