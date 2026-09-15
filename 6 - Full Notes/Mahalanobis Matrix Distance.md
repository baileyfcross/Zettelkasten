2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Distance Framework]]

# Mahalanobis Matrix Distance

MahalanobisDistance measures a difference vector after transformation by a stored matrix related to inverse covariance. Correlated numeric directions are scaled jointly rather than treated as independent axes.

The class checks schema and matrix dimensions, builds component differences, multiplies them with Boost uBLAS, and returns the transformed norm. A singular or poorly estimated covariance matrix requires regularization before constructing the strategy.

# References

[[dataclusteringincplusplus.pdf]]

