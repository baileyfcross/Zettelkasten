2026-09-13 10:25

Status: #baby

Tags: [[Outlier Detection and DBSCAN]]

# DBSCAN

DBSCAN is a density-based clustering algorithm that grows clusters from points with sufficiently populated radius neighborhoods. It discovers arbitrarily shaped groups and labels observations outside dense regions as noise.

The algorithm does not require the number of clusters in advance. Its radius, minimum-point threshold, and distance measure must match the data's scale and density structure.

The neighborhood tests, distance matrix work, and recursive expansion are more control-intensive than a simple centroid assignment. FPGA acceleration can reuse distance hardware, but the varying number of neighbors and recursive growth make workload balance and memory access central constraints.

# References

[[clusteranalysisanddatamining.pdf]]

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]
