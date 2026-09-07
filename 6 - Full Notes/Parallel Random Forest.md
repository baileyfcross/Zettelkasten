2026-09-06 22:42

Status: #baby

Tags: [[Hospital Big Data Analytics]]

# Parallel Random Forest

A parallel random forest trains or evaluates multiple decision trees across workers. Independent bootstrap samples and candidate feature selections expose substantial parallelism, after which tree predictions are aggregated.

On a Spark platform, distributing tree construction can handle large hospital datasets, though data partitioning, repeated scans, and model collection still affect runtime.

# References

[[bigdatamanagementandprocessing.pdf]]
