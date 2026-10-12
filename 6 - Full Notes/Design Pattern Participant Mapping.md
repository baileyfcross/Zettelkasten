2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Design Patterns]]

# Design Pattern Participant Mapping

A design pattern becomes concrete only after each abstract participant is mapped to a class and responsibility in the application. For a clustering Composite, Node is the component, LeafNode is the leaf, and InternalNode is the composite that owns children.

Writing the mapping prevents pattern names from replacing design reasoning. It clarifies which object controls creation, which interface clients use, and which dependency is intended to vary.

# References

[[dataclusteringincplusplus.pdf]]

