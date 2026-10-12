2026-09-14 22:06

Status: #baby

Tags: [[C++ Hierarchical Clustering Implementation]]

# Pairwise Distance Matrix Construction

The LW create_dm operation computes each pairwise record distance once and stores it in a symmetric two-key map. These singleton distances initialize the intercluster values used by the first agglomerative merge.

Building the matrix up front simplifies repeated nearest-pair searches at the cost of quadratic storage and calculation. A proxy distance matrix could replace raw record computation if the input contract were extended.

# References

[[dataclusteringincplusplus.pdf]]

