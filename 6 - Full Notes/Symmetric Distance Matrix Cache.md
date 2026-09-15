2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Distance Framework]]

# Symmetric Distance Matrix Cache

A symmetric distance matrix cache stores each pairwise value once under an unordered or normalized pair of record or cluster identifiers. Agglomerative methods consult and update this structure repeatedly as clusters merge.

Avoiding duplicate calculations nearly halves storage relative to a full directed map and removes redundant distance calls. Insertion, lookup, and deletion rules must consistently treat the two key orders as the same pair.

# References

[[dataclusteringincplusplus.pdf]]

