2026-09-14 21:34

Status: #baby

Tags: [[Stream and Big Data Clustering]]

# Clustering Feature Microcluster

A clustering feature summarizes a set of numeric points by its count, coordinate-wise linear sum, and squared sum. These quantities are additive, so summaries from disjoint groups can be merged without revisiting their members.

Centroids, radii, and within-group dispersion can be derived from the tuple. The summary is efficient but cannot reconstruct arbitrary shapes or distributions, so compression is most faithful for compact local groups.

# References

[[dataclustering.pdf]]

