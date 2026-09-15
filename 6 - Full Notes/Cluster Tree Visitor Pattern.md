2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Design Patterns]]

# Cluster Tree Visitor Pattern

The Visitor pattern moves operations on a node hierarchy into a separate class family. Each leaf or internal node accepts a NodeVisitor and dispatches to the overload matching its concrete node type.

ClusLib uses visitors to collect join values, build flat partitions, and draw dendrograms without embedding every operation in Node. Adding a new visitor is easy, while adding a new node type requires changing the visitor interface and each concrete visitor.

# References

[[dataclusteringincplusplus.pdf]]

