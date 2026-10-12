2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Distance Framework]]

# C++ Distance Strategy Interface

Distance is an abstract binary function over two shared Record pointers that returns a real dissimilarity. A virtual call operator supplies the strategy extension point, and an immutable name identifies the concrete measure.

Clustering algorithms can depend on this narrow callable interface rather than on formulas. The strategy is replaceable when the algorithm's assumptions permit, and its virtual destructor supports ownership through the base pointer.

# References

[[dataclusteringincplusplus.pdf]]

