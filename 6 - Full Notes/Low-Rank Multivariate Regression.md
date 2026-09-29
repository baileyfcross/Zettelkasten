2026-09-29 19:17

Status: #baby

Tags: [[Sparse and Structured Regression]]

# Low-Rank Multivariate Regression

Low-rank multivariate regression assumes the coefficient or fitted-response matrix is governed by a small number of latent response directions. When the rank is known, the constrained least-squares fit is obtained by truncating the singular value decomposition of the response projected onto the design space.

The prediction error decomposes into the singular-value tail left out by the rank constraint and a variance term that grows with retained rank. This makes rank a complexity parameter analogous to support size in sparse regression and motivates [[Rank-Adaptive Estimation]] when the true rank is unknown.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
