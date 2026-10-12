2026-09-14 22:06

Status: #baby

Tags: [[C++ Hierarchical Clustering Implementation]]

# DIANA Splinter Group Implementation

DIANA implements divisive hierarchy construction by selecting an unsplit cluster with large diameter and creating a splinter group. It first moves the record with greatest average dissimilarity from the remainder, then transfers other records when they are closer on average to the splinter.

The final two sets become child clusters and the process repeats. Splitting the largest-diameter cluster produces a monotonic hierarchy but remains sensitive to outlying records.

# References

[[dataclusteringincplusplus.pdf]]

