2026-09-29 19:17

Status: #baby

Tags: [[Sparse and Structured Regression]]

# Adaptive Lasso

Adaptive Lasso applies coefficient-specific $\ell_1$ weights, penalizing a coordinate inversely to the magnitude of an initial estimate. Large preliminary coefficients receive a smaller penalty, while weak or absent coordinates are penalized more strongly.

Using a [[Gauss-Lasso]] estimate for the weights produces a convex second-stage problem that approximates a nonconvex count penalty more closely than ordinary Lasso. The method aims to reduce [[Lasso Shrinkage Bias]] and improve support selection, but its result depends on the quality of the preliminary estimator.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
