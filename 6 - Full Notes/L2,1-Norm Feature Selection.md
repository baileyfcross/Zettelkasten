2026-10-07 00:46

Status: #baby

Tags: [[Multivariate Spectral Feature Selection]]

# L2,1-Norm Feature Selection

L2,1-norm feature selection penalizes a coefficient matrix by summing the Euclidean norms of its rows. Increasing the penalty drives entire rows to zero, so one input feature is removed from every output task at once.

Applied to [[Multi-Output Regression Feature Selection]], this row-level sparsity makes the selected predictors jointly explain several target directions. It differs from elementwise sparsity, which can select a different predictor set for each output and may leave many predictors active across the matrix as a whole.

# References

[[spectralfeatureselectionfordatamining.pdf]]

