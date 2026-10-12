2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Result Modeling]]

# Partitional Clustering Container

PClustering is a container of shared Cluster pointers representing one flat partition. It can remove empty clusters, assign cluster identifiers, save assigned records, calculate cluster sizes, and compare memberships with any labels supplied in the dataset.

Storing base pointers lets the same partition contain derived center or subspace clusters. Calculated summaries should be invalidated when membership changes so output does not mix current clusters with stale counts.

# References

[[dataclusteringincplusplus.pdf]]

