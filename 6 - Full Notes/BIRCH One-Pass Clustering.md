2026-09-14 21:34

Status: #baby

Tags: [[Stream and Big Data Clustering]]

# BIRCH One-Pass Clustering

BIRCH incrementally inserts observations into a height-balanced clustering-feature tree. Leaf entries summarize compact subclusters, and a threshold controls whether a new point can be absorbed or requires a new entry.

A single scan can compress a large dataset into memory before a global clusterer is applied to leaf summaries. Input order and the absorption threshold affect the tree, and non-spherical structures may be poorly represented by compact statistics.

# References

[[dataclustering.pdf]]

