2026-09-29 19:17

Status: #baby

Tags: [[Sparse and Structured Regression]]

# Lasso Estimator

The Lasso estimator minimizes squared residual error plus an $\ell_1$ penalty on regression coefficients. It replaces the nonconvex count of nonzero coefficients with a convex surrogate, making sparse high-dimensional regression computationally tractable.

As the penalty increases, more coefficients become exactly zero and the fitted signal is also shrunk toward zero. The method therefore performs estimation and variable selection together. Its statistical performance depends on the tuning parameter, noise level, and geometry of the design, summarized in bounds through quantities such as the [[Compatibility Constant]].

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
