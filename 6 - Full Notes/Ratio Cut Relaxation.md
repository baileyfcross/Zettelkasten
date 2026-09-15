2026-09-14 21:34

Status: #baby

Tags: [[Matrix Factorization and Spectral Clustering]]

# Ratio Cut Relaxation

Ratio cut measures a graph partition by summing the cut weight for each group after dividing by the number of vertices in that group. The balance term penalizes solutions that create tiny isolated clusters.

Optimizing the discrete objective exactly is difficult. A spectral relaxation replaces discrete membership indicators with continuous vectors, solves an eigenvector problem, and then rounds the embedding back to cluster assignments.

# References

[[dataclustering.pdf]]

