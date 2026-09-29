2026-09-29 19:17

Status: #baby

Tags: [[Sparse and Structured Regression]]

# Multivariate Linear Regression

Multivariate linear regression predicts a vector response from a common set of covariates, writing the observations as $Y=XA+E$. Each response coordinate could be fitted separately, but joint estimation can exploit structure shared across the columns of the coefficient matrix $A$.

Shared structure may take the form of common selected predictors, represented by nonzero rows, or a common low-dimensional response space, represented by low rank. Joint analysis is most valuable when these restrictions are scientifically plausible; otherwise it can couple unrelated response coordinates and add unnecessary bias.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
