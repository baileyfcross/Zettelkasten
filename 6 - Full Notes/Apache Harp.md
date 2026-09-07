2026-09-06 22:09

Status: #baby

Tags: [[Scalable Social Data Processing]]

# Apache Harp

Apache Harp is presented as a Hadoop plug-in that adds long-running map workers and [[Collective Communication]] for iterative computations. Its MapCollective interface lets a program retain processes and reusable data across repeated rounds.

The book integrates Harp with Pig so high-level scripts can run K-means and PageRank without restarting a complete Hadoop job for every iteration. The resulting workflow exchanges partial updates in memory.

# References

[[bigdataincomplexandsocialnetworks.pdf]]
