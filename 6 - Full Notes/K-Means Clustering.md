2026-09-06 22:09

Status: #baby

Tags: [[Scalable Social Data Processing]] · [[Partition and K-Means Clustering]]

# K-Means Clustering

K-means clustering partitions multidimensional data by repeatedly assigning each point to its nearest centroid and recomputing centroids from the assigned points. Distance calculations and centroid aggregation continue until a stopping condition is met.

At scale, points can remain cached on distributed workers while partial centroid sums are combined through [[Collective Communication]]. Its repeated structure makes K-means a useful benchmark for [[Iterative Data Processing]].

The source distinguishes update variants: MacQueen updates centroids after each reallocation, while Forgy holds seeds fixed for a full allocation pass and then recomputes centers. All can converge to a local optimum determined by the initial partition, so repeated starts and comparison of final squared-error values are part of responsible use.

# References

[[bigdataincomplexandsocialnetworks.pdf]]

[[clusteranalysisanddatamining.pdf]]
