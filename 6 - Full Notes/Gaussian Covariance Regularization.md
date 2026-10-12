2026-09-14 22:06

Status: #baby

Tags: [[C++ Specialized Clustering Implementations]]

# Gaussian Covariance Regularization

Gaussian covariance regularization adds a nonnegative epsilon term to covariance estimates before inversion or likelihood evaluation. It prevents a component concentrated on too few or collinear points from producing a singular matrix.

The parameter trades numerical stability against fidelity to the unregularized maximum-likelihood estimate. It should be reported because changing epsilon can alter responsibilities, convergence, and the selected clustering.

# References

[[dataclusteringincplusplus.pdf]]

