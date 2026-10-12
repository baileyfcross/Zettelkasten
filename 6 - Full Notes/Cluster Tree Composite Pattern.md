2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Design Patterns]]

# Cluster Tree Composite Pattern

The Composite pattern represents individual leaves and nested groups through one node interface. In a clustering tree, LeafNode stores a record and InternalNode stores child nodes, while both answer traversal and size operations through their common Node base.

Clients can treat a complete hierarchy and a single leaf uniformly, which simplifies partition extraction and rendering. Parent links, child ownership, levels, and join values must remain consistent as nodes are combined.

# References

[[dataclusteringincplusplus.pdf]]

