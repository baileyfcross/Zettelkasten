2026-09-06 22:42

Status: #baby

Tags: [[Distributed Data Mining and Clustering]]

# MapReduce-Based Mining

MapReduce-based mining divides data or candidate evaluation among mapper tasks and combines local results in reducers. The model provides cluster distribution and failure recovery for scans over large collections.

Repeated mining passes can incur substantial job startup, shuffle, and disk costs, so algorithm design should reduce iterations and the amount of intermediate data.

# References

[[bigdatamanagementandprocessing.pdf]]
