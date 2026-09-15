2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Dataset Modeling]]

# ClusLib Attribute Information Base

AttrInfo is the polymorphic metadata base for an attribute. It records common identity and type behavior and defines virtual operations for setting, retrieving, comparing, and measuring values through the corresponding AttrValue objects.

Continuous and discrete subclasses implement type-specific semantics behind that interface. Algorithms can traverse a schema uniformly while runtime dispatch selects the correct handling for each component.

# References

[[dataclusteringincplusplus.pdf]]

