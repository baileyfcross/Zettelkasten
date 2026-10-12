2026-09-09 03:12

Status: #baby

Tags: [[Partition and K-Means Clustering]]

# Cluster Feature Tree

A cluster feature tree is a height-balanced hierarchy that stores [[Cluster Feature Vector|cluster feature vectors]]. Internal entries point to child summaries, while leaf entries represent bounded-diameter subclusters and are connected for later global clustering.

Branching and diameter thresholds control memory and compression. Inserting a point updates ancestor summaries and may split nodes or increase the tree height.

# References

[[clusteranalysisanddatamining.pdf]]

