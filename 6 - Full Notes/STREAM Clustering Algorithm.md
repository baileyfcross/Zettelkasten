2026-09-14 21:34

Status: #baby

Tags: [[Stream and Big Data Clustering]]

# STREAM Clustering Algorithm

STREAM processes a large sequence in manageable batches. Each batch is clustered locally, its centers are retained as weighted representatives, and those representatives are periodically reclustered to form the final solution.

The approach converts a memory-intensive problem into repeated clustering of bounded summaries. Approximation quality depends on how well weighted centers preserve the original geometry and on how errors accumulate across compression levels.

# References

[[dataclustering.pdf]]

