2026-09-14 22:06

Status: #baby

Tags: [[C++ Hierarchical Clustering Implementation]]

# Single and Complete Linkage Subclasses

Single and Complete are LW subclasses whose only distinctive implementation is the distance update. Single linkage retains the minimum distance from either merged child, while complete linkage retains the maximum.

The tiny subclasses demonstrate successful Template Method design: the common matrix, forest, merge, and result code is inherited, and the choice between chaining and compactness is localized to one recurrence.

# References

[[dataclusteringincplusplus.pdf]]

