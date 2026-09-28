2026-09-28 03:43

Status: #baby

Tags: [[Recommendation Hardware Acceleration]]

# Item-Based Collaborative Filtering Hardware

Item-based collaborative filtering hardware computes similarities between item-rating vectors and uses neighboring items to predict a user's score. The arithmetic resembles user-based hardware, allowing a common [[Similarity Metric Accelerator]] to support both.

Item vectors may have a different length and sparsity from user vectors. The same fixed parallel structure can therefore achieve a different utilization and speedup on the two orientations of the rating matrix.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

