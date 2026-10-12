2026-09-14 22:06

Status: #baby

Tags: [[C++ Specialized Clustering Implementations]]

# MPI K-Means Data Distribution

The parallel K-means implementation uses a Boost MPI communicator to divide records among processes. The master reads the dataset, converts its numeric values to contiguous vectors, sends each worker a balanced block, and retains its own block.

Every process stores the shared centers but computes assignments only for local records. Uneven division gives at most one extra record to earlier ranks, limiting load imbalance from record count.

# References

[[dataclusteringincplusplus.pdf]]

