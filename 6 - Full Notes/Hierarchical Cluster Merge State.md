2026-09-14 22:06

Status: #baby

Tags: [[C++ Hierarchical Clustering Implementation]]

# Hierarchical Cluster Merge State

A hierarchical merge joins two HClustering roots under a new internal node, records their join value, combines their sizes, and updates active cluster identifiers. Old distance entries are removed and new distances are inserted.

Keeping forest, size map, active set, and distance cache synchronized is essential. A partial update can leave the next nearest-pair search referring to a cluster that no longer exists.

# References

[[dataclusteringincplusplus.pdf]]

