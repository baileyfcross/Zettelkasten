2026-09-29 19:17

Status: #baby

Tags: [[Sparse and Structured Regression]] · [[Multivariate Spectral Feature Selection]]

# Row-Sparse Multivariate Regression

Row-sparse multivariate regression assumes that every response depends on the same small subset of predictors. In the coefficient matrix, predictors outside that subset have entire zero rows.

Stacking the response columns turns the problem into [[Group Lasso]], with one group containing a predictor's coefficients across all responses. The group penalty selects predictors jointly and can borrow evidence across response coordinates. This assumption differs from ordinary coordinate sparsity, which could allow a completely different selected set for each response.

An L2,1 penalty implements this structure by summing the Euclidean norms of coefficient rows. In spectral feature selection, several weighted eigenvectors of a target similarity matrix become the responses, so nonzero rows identify one shared feature subset that preserves multiple structural directions together.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]

[[spectralfeatureselectionfordatamining.pdf]]
