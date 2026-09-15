2026-09-14 22:06

Status: #baby

Tags: [[C++ Hierarchical Clustering Implementation]]

# Closest Cluster Pair Selection

At each agglomerative step, the linkage routine finds the smallest stored distance among currently unmerged clusters. It removes the chosen pair from active state and uses their distance as the join value of a new parent.

A straightforward scan is simple but can dominate runtime as the matrix grows. Whatever selection structure is used must ignore obsolete pairs after clusters are merged.

# References

[[dataclusteringincplusplus.pdf]]

