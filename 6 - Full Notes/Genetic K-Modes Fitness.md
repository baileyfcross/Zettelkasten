2026-09-14 22:06

Status: #baby

Tags: [[C++ Specialized Clustering Implementations]]

# Genetic K-Modes Fitness

Genetic K-modes fitness converts within-cluster categorical dissimilarity into a score used to compare chromosomes. Better candidates assign records closer to their corresponding mode and therefore receive greater reproductive influence.

A fitness transformation must remain well behaved when objective values are zero or very similar. The reported final objective should retain its original scale even if selection uses a transformed score.

# References

[[dataclusteringincplusplus.pdf]]

