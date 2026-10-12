2026-09-13 10:25

Status: #baby

Tags: [[Outlier Detection and DBSCAN]]

# Relative Density Outlier Score

A relative density outlier score compares the density around a point with the average density around its neighbors. A point whose local density is low relative to that context receives a stronger anomaly score.

The comparison provides a ranking rather than only a yes-or-no decision. Selecting k remains difficult, and a direct implementation can require quadratic computation.

# References

[[clusteranalysisanddatamining.pdf]]

