2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Result Modeling]]

# ClusLib Results Object

Results contains the hard cluster membership vector and inherits a map for named algorithm-specific outputs. Its reset operation clears both the common vector and the additional result values before a fresh result is published.

Clients receive a const reference so they can inspect but not rewrite the algorithm's answer. Centers, hierarchies, errors, likelihoods, iterations, or fuzzy matrices can be returned under explicit keys.

# References

[[dataclusteringincplusplus.pdf]]

