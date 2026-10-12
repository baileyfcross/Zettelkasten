2026-09-09 03:12

Status: #baby

Tags: [[Partition and K-Means Clustering]]

# Jancey's K-Means Method

Jancey's K-means method assigns observations to the nearest class point, then obtains each new class point by reflecting the old point through the new cluster centroid. Passes continue until moving observations no longer improves the solution.

The method implicitly minimizes a within-cluster error function. Like other K-means variants, it can require several initial configurations to explore alternative local optima.

# References

[[clusteranalysisanddatamining.pdf]]

