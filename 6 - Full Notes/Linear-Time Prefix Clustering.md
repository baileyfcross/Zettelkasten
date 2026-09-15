2026-09-15 10:22

Status: #baby

Tags: [[Scalable Hierarchical Search]]

# Linear-Time Prefix Clustering

Prefix clustering assigns each encoded record to the branches determined by its successive digits. The book argues that a Baire hierarchy can be read in one scan of the input rather than constructed from all pairs of observations, which ordinary agglomerative clustering often requires.

The linear-time claim applies to the scan when code length or measurement precision is treated as bounded. A useful comparison must still account for the cost of creating codes, random projections for multidimensional data, storage, and any later refinement of coarse bins. Speed does not guarantee the bins reflect the intended domain similarity.

# References

[[datasciencefoundations_geometry.pdf]]
