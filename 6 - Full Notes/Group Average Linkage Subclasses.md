2026-09-14 22:06

Status: #baby

Tags: [[C++ Hierarchical Clustering Implementation]]

# Group Average Linkage Subclasses

Group-average linkage weights child-to-cluster distances by the child cluster sizes, whereas weighted group average gives the two merged children equal influence regardless of size. Both fit the LW update interface.

The size map supplies the coefficients needed by the ordinary average method. Separating the formulas into subclasses prevents conditionals for every linkage from accumulating in the main merge loop.

# References

[[dataclusteringincplusplus.pdf]]

