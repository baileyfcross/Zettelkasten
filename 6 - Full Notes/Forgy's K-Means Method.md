2026-09-09 03:12

Status: #baby

Tags: [[Partition and K-Means Clustering]]

# Forgy's K-Means Method

Forgy's K-means method holds seed points fixed while allocating a complete pass of observations, then replaces the seeds with the centroids of the resulting clusters. Allocation and recomputation alternate until memberships stop changing.

Batch updates make each iteration easy to understand, but the converged partition remains sensitive to the initial seeds and the chosen value of k.

# References

[[clusteranalysisanddatamining.pdf]]

