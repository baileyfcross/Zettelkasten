2026-09-29 19:17

Status: #baby

Tags: [[Sparse and Structured Regression]]

# Rank-Adaptive Estimation

Rank-adaptive estimation selects the effective rank of a matrix estimator from data instead of assuming it known. A penalized criterion balances residual error against a variance cost proportional to rank and the dimensions of the projected response matrix.

Because all rank-constrained fits can be derived from one singular value decomposition, the candidate collection is computationally manageable. An oracle bound compares the selected estimate with the best bias–variance tradeoff over ranks. This is a tractable instance of [[Penalized Model Selection]] even though joint rank-and-support selection can be intractable.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
