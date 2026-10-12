2026-09-28 03:43

Status: #baby

Tags: [[Partition and K-Means Clustering]]

# Partitioning Around Medoids

Partitioning Around Medoids, or PAM, assigns points to one of $k$ clusters but represents each cluster by an observed data object rather than an arithmetic mean. The next medoid is the member that minimizes total distance to the other members of its cluster.

Using an observed representative makes PAM less sensitive to noise and isolated values than a mean-based center. The repeated candidate-distance sums are more expensive, so the method can become costly on large datasets.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]
