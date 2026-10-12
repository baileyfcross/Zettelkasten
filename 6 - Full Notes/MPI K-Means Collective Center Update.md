2026-09-14 22:06

Status: #baby

Tags: [[C++ Specialized Clustering Implementations]]

# MPI K-Means Collective Center Update

During each parallel iteration, every process calculates local membership changes, coordinate sums, and cluster sizes. Collective all-reduce operations add those vectors across ranks, after which every process divides global sums by global sizes to obtain identical new centers.

When convergence ends, workers send membership vectors to the master and a reduction collects objective contributions. Communication cost and serial input or output limit the speedup even when assignment work scales across processors.

# References

[[dataclusteringincplusplus.pdf]]

