2026-10-07 00:46

Status: #baby

Tags: [[Multivariate Spectral Feature Selection]]

# Multi-Output Regression Feature Selection

Multi-output regression feature selection treats several target vectors as columns of one response matrix and chooses predictors that explain them jointly. In spectral selection, weighted eigenvectors of a target similarity operator supply these outputs.

The residual is measured with the Frobenius norm, while an [[L2,1-Norm Feature Selection]] penalty creates shared row sparsity in the coefficient matrix. The result is a feature subset whose linear combinations preserve several spectral directions together rather than optimizing each feature independently.

# References

[[spectralfeatureselectionfordatamining.pdf]]

