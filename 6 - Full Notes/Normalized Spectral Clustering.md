2026-09-14 21:34

Status: #baby

Tags: [[Matrix Factorization and Spectral Clustering]]

# Normalized Spectral Clustering

Normalized spectral clustering rescales the graph Laplacian by vertex degrees before extracting its eigenvectors. The normalization relates graph separation to the volume of a region rather than only the raw number or weight of cut edges.

This discourages trivial cuts that isolate a few low-degree vertices and often handles unequal graph density better. Very small degrees and disconnected components still require care during normalization and interpretation.

# References

[[dataclustering.pdf]]

