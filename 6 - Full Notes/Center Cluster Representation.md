2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Result Modeling]]

# Center Cluster Representation

CenterCluster extends Cluster with a shared pointer to a representative Record and accessors for reading or updating it. Center-based algorithms can therefore return both membership and the prototype used to define each group.

The center should be a distinct record object rather than a pointer to one dataset member. Otherwise updating the prototype during an iteration would silently overwrite an input observation.

# References

[[dataclusteringincplusplus.pdf]]

