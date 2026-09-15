2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Result Modeling]]

# Leaf and Internal Cluster Nodes

LeafNode stores one shared Record and reports zero children and one record. InternalNode combines Node with a container of child-node pointers and stores the join value at which its descendants became one group.

The pair implements the Composite pattern: both participate through Node, but only the internal form owns descendants. InternalNode's multiple inheritance combines tree identity with reusable typed-container behavior.

# References

[[dataclusteringincplusplus.pdf]]

