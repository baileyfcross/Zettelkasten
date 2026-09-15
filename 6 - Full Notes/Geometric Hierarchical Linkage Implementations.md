2026-09-14 22:06

Status: #baby

Tags: [[C++ Hierarchical Clustering Implementation]]

# Geometric Hierarchical Linkage Implementations

Centroid, median, and Ward subclasses implement Lance-Williams recurrences tied to representative geometry or changes in within-cluster dispersion. Their coefficients use cluster sizes and can differ from purely pairwise minimum or maximum rules.

Centroid and median methods may produce nonmonotonic dendrogram inversions, while Ward favors compact variance-minimizing merges. The tree representation preserves the actual join values even when they do not rise monotonically.

# References

[[dataclusteringincplusplus.pdf]]

