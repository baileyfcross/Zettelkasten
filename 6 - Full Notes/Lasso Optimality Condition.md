2026-09-29 19:17

Status: #baby

Tags: [[Sparse and Structured Regression]]

# Lasso Optimality Condition

The Lasso optimality condition sets zero inside the subdifferential of the squared-error loss plus the $\ell_1$ penalty. For a nonzero coefficient the penalty subgradient equals its sign; for a zero coefficient it may take any value between minus one and one.

This condition gives a threshold rule under an orthonormal design: a coordinate remains zero when its correlation with the response is below the penalty threshold, and otherwise it is soft-thresholded. With correlated predictors there is no independent coordinate formula, but the same condition underlies algorithms and the [[Lasso Oracle Inequality]].

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
