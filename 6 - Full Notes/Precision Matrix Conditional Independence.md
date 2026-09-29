2026-09-29 19:17

Status: #baby

Tags: [[High-Dimensional Graphical Models]]

# Precision Matrix Conditional Independence

For a nonsingular multivariate Gaussian distribution, a zero off-diagonal entry in the precision matrix $K=\Sigma^{-1}$ means that the corresponding variables are conditionally independent given all remaining variables. Nonzero entries define the edges of the minimal [[Gaussian Graphical Model]].

The same structure appears in linear prediction: each variable can be regressed on the others with coefficients proportional to a column of $K$. This equivalence supports both precision-matrix methods such as [[Graphical Lasso]] and regression-based neighborhood selection.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
