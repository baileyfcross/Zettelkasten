2026-09-17 09:48

Status: #baby

Tags: [[Recommender System Evolution]]

# Memory-Based Collaborative Filtering

Memory-based collaborative filtering uses the available interaction dataset directly when calculating a recommendation. It commonly compares users or items by similarity and combines the preferences of nearby cases.

The method is intuitive because predictions can be traced to observed neighbors. Its computation and storage can become expensive as the user-item dataset grows.

User-based and item-based variants orient the same sparse interaction matrix differently. Both repeatedly intersect rating vectors, compute a similarity, and combine neighborhood evidence; the regular statistical structure makes their shared kernels suitable for a [[Similarity Metric Accelerator]].

# References

[[frontiersofdatascience.pdf]]

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]
