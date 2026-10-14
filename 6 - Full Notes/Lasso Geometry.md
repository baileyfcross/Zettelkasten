2026-09-29 19:17

Status: #baby

Tags: [[Sparse and Structured Regression]]

# Lasso Geometry

Lasso geometry views penalized regression as minimizing squared error inside an $\ell_1$ ball. The ball has corners on coordinate axes, so expanding an elliptical loss contour often first touches the feasible set where one or more coefficients are exactly zero.

This nonsmooth boundary explains why an $\ell_1$ constraint selects variables, while a smooth $\ell_2$ ball generally shrinks coefficients without producing exact zeros. The geometric picture is equivalent to the penalized [[Lasso Estimator]] for a corresponding radius and also makes the source of [[Lasso Shrinkage Bias]] visible.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
