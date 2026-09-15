2026-09-14 22:06

Status: #baby

Tags: [[C++ Partitional and Fuzzy Clustering]]

# C++ K-Means Assignment Iteration

A Kmean iteration updates centers from current memberships and then reassigns every record to the closest center under the configured distance. The loop continues until no membership changes or the maximum iteration count is exceeded.

The assignment count supplies a direct convergence test, while the final squared-error objective summarizes compactness. Empty clusters require explicit handling because their centers cannot be updated from member averages.

# References

[[dataclusteringincplusplus.pdf]]

