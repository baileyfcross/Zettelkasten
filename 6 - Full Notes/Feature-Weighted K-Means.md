2026-09-14 21:34

Status: #baby

Tags: [[Unsupervised Feature Selection for Clustering]]

# Feature-Weighted K-Means

Feature-weighted K-means extends the usual partitioning objective by learning how strongly each dimension contributes to distance. Cluster assignments, centroids, and feature weights are updated so that informative dimensions receive greater influence.

Some variants learn one global weight vector, while others allow each cluster to emphasize a different subspace. Without regularization, weights can collapse onto a few dimensions, so constraints or penalties are used to maintain a useful balance.

# References

[[dataclustering.pdf]]

