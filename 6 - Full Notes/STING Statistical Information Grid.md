2026-09-14 21:34

Status: #baby

Tags: [[Density and Grid-Based Clustering]]

# STING Statistical Information Grid

STING divides space into hierarchical cells and stores statistical summaries such as count, mean, variance, minimum, maximum, and distribution type for each cell. Queries and cluster decisions can then operate on summaries rather than raw points.

Higher-level cell statistics can be derived from children, enabling fast top-down pruning. The efficiency comes at the cost of axis-aligned boundaries and possible loss of fine structure inside summarized cells.

# References

[[dataclustering.pdf]]

