2026-09-29 19:17

Status: #baby

Tags: [[Sparse and Structured Regression]]

# Compatibility Constant

The compatibility constant measures how well the design matrix separates sparse coefficient changes from changes outside a candidate support. It lower-bounds prediction-space movement relative to the $\ell_1$ size of the supported coefficients inside a cone where off-support error is controlled.

A small value indicates that correlated columns can cancel, making coefficients hard to identify and weakening sparse-regression guarantees. The constant appears in the denominator of a [[Lasso Oracle Inequality]], so good prediction bounds require more than sparsity alone. Group-sparse methods use an analogous quantity based on sums of group norms.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
