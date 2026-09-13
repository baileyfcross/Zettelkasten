2026-09-13 10:20

Status: #baby

Tags: [[Fuzzy Clustering]]

# Fuzzy Membership Matrix

A fuzzy membership matrix records the membership degree of every observation in every cluster. Rows correspond to observations and columns to clusters.

Fuzzy C-means repeatedly updates this matrix from distances to the current centers, then recomputes centers from the updated memberships. Convergence is assessed by comparing successive matrices.

# References

[[clusteranalysisanddatamining.pdf]]

