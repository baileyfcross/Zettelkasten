2026-09-16 01:38

Status: #baby

Tags: [[Advanced Feature Selection]] · [[Sparse and Structured Regression]]

# Sparsity-Based Feature Selection

Sparsity-based feature selection adds a constraint or penalty that drives many model coefficients to zero. The remaining nonzero dimensions form an embedded feature subset.

Sparse objectives combine prediction and selection in one optimization problem and can scale better than explicit subset enumeration. Correlated inputs, penalty strength, and grouped structure influence which variables survive.

The [[Lasso Estimator]] is the canonical convex implementation for coordinate sparsity. Related penalties select predefined groups or a small number of coefficient changes, while multivariate extensions select whole predictor rows. These methods replace combinatorial support counts with norms that are feasible to optimize but can introduce shrinkage and depend on design geometry.

# References

[[featureengineeringformachinelearninganddataanalytics.pdf]]

[[introductiontohigh-dimensionalstatistics.pdf]]
