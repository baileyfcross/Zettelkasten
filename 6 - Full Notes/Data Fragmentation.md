2026-09-06 22:42

Status: #baby

Tags: [[Hadoop and SQL Analytics]]

# Data Fragmentation

Data fragmentation divides a relation or dataset into pieces that can be stored and processed separately. Horizontal fragmentation separates rows, while vertical fragmentation separates groups of columns while retaining a way to reconstruct the original relation.

Distribution can improve parallelism and locality, but queries that cross fragments pay communication and coordination costs.

# References

[[bigdatamanagementandprocessing.pdf]]
