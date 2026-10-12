2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Result Modeling]]

# Cluster Membership Vector Representation

A cluster membership vector stores, at position i, the index of the cluster assigned to record i. It is a compact representation for hard partitions and is used as the common result field across ClusLib algorithms.

The vector assumes a stable record order and cluster-index convention. Fuzzy memberships, hierarchy, centers, or diagnostics require additional structures because one integer per record cannot express them.

# References

[[dataclusteringincplusplus.pdf]]

