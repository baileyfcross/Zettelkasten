2026-09-14 21:34

Status: #baby

Tags: [[Stream and Big Data Clustering]]

# MapReduce Co-Clustering

MapReduce co-clustering distributes the updates needed to group rows and columns of a large matrix. Mapping stages compute local assignments or sufficient statistics, and reduction stages aggregate them into updated row and column models.

The design suits sparse document, graph, or transactional matrices whose entries can be partitioned. Iterative synchronization and data shuffling may dominate cost, so algorithms minimize passes while retaining globally consistent summaries.

# References

[[dataclustering.pdf]]

