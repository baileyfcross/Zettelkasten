2026-09-14 22:06

Status: #baby

Tags: [[C++ Partitional and Fuzzy Clustering]]

# Multiple-Seed K-Means Execution

Multiple-seed execution constructs a fresh Kmean object for each run, supplies a different positive seed, and records both its iterations and objective value. Fresh objects prevent mutable internal state from one run affecting the next.

Repeating the algorithm addresses initialization sensitivity rather than changing the local optimization. The set of seeds and number of runs are part of the experiment and should be reported with the result.

# References

[[dataclusteringincplusplus.pdf]]

