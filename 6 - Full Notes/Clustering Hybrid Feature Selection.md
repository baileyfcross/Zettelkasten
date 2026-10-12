2026-09-14 21:34

Status: #baby

Tags: [[Unsupervised Feature Selection for Clustering]]

# Clustering Hybrid Feature Selection

A hybrid feature-selection method combines a fast filter with a clustering-aware refinement. The filter narrows the candidate set, and a wrapper or embedded stage then tests how the surviving features affect cluster structure.

This design reduces the search cost of a pure wrapper while retaining more task sensitivity than a standalone filter. Its result depends on both stages, so the filtering threshold must not discard dimensions that become useful only in combination.

# References

[[dataclustering.pdf]]

