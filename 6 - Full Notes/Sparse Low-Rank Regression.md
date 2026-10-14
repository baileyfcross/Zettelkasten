2026-09-29 19:17

Status: #baby

Tags: [[Sparse and Structured Regression]]

# Sparse Low-Rank Regression

Sparse low-rank regression assumes that a multivariate coefficient matrix has both few active rows and small rank. Row sparsity selects a shared subset of predictors, while low rank represents the responses through a small number of common directions.

Using both structures can in principle improve accuracy beyond either alone. Exact joint model selection is combinatorial, and adding group and nuclear-norm penalties gives a convex criterion but does not automatically deliver the sharper risk bound suggested by the ideal selector. The method illustrates the gap between a plausible structural objective and a proven computational relaxation.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
