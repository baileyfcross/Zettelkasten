2026-09-14 22:06

Status: #baby

Tags: [[C++ Hierarchical Clustering Implementation]]

# Linkage Distance Update Hook

update_dm receives the identifiers of two merged clusters and their replacement, then computes distances between the replacement and every other active cluster. It is pure virtual in LW because the formula defines the linkage method.

Derived implementations reuse stored distances and cluster sizes rather than revisit all underlying records. This hook is the narrow mathematical variation point in the agglomerative family.

# References

[[dataclusteringincplusplus.pdf]]

