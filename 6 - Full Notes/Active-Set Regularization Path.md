2026-10-07 00:46

Status: #baby

Tags: [[Multivariate Spectral Feature Selection]]

# Active-Set Regularization Path

An active-set regularization path tracks how a sparse model changes as its penalty decreases. Instead of testing many unrelated penalty values, it computes the next point at which an inactive feature satisfies the entry condition and updates only the currently relevant variables.

For [[Minimal Redundancy Spectral Feature Selection]], the path begins with the feature most correlated with the target residual. A walking direction and step size identify a tentative entrant, a smaller optimization problem refines the coefficients, and the [[Equal-Correlation Optimality Condition]] checks the result against the full feature set.

# References

[[spectralfeatureselectionfordatamining.pdf]]

