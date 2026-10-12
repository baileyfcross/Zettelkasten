2026-09-14 21:34

Status: #baby

Tags: [[High-Dimensional and Subspace Clustering]]

# ORCLUS Clustering

ORCLUS finds projected clusters in arbitrarily oriented subspaces. It begins with many seed clusters in the full space, estimates low-variance directions, and repeatedly merges clusters while reducing both the cluster count and subspace dimensionality.

Local covariance eigenvectors define each cluster's preferred orientation. This captures correlated structures beyond axis-parallel methods, but covariance estimation can be unstable for small or noisy intermediate groups.

# References

[[dataclustering.pdf]]

