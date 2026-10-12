2026-09-28 03:43

Status: #baby

Tags: [[Hierarchical Clustering Methods]]

# SLINK Clustering

SLINK clustering is a single-link hierarchical method that repeatedly merges the two clusters connected by the smallest intercluster distance. A distance threshold can stop merging without requiring the final number of clusters in advance.

The method can recover nonspherical organization, but its distance updates and minimum searches are time-consuming, and single linkage is vulnerable to chaining through unusual points. Hardware can accelerate common distance operations without removing those algorithmic properties.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]
