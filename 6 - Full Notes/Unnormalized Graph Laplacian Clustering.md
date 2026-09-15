2026-09-14 21:34

Status: #baby

Tags: [[Matrix Factorization and Spectral Clustering]]

# Unnormalized Graph Laplacian Clustering

The unnormalized graph Laplacian is the degree matrix minus the similarity matrix. Its low-valued eigenvectors encode directions in which strongly connected vertices vary together and weakly connected regions can separate.

Spectral clustering embeds vertices using selected eigenvectors and partitions that embedding, often with K-means. The unnormalized form can behave poorly when vertex degrees vary greatly because high- and low-degree regions contribute on different scales.

# References

[[dataclustering.pdf]]

