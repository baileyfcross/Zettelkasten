2026-09-06 22:42

Status: #baby

Tags: [[Hadoop and SQL Analytics]]

# Resilient Distributed Dataset

A resilient distributed dataset is Spark's partitioned collection abstraction for parallel transformations and actions. It can cache working data in memory and records lineage so a lost partition can be recomputed from earlier transformations.

Immutability and lineage simplify recovery, while partitioning and persistence choices determine locality, communication, and memory pressure.

# References

[[bigdatamanagementandprocessing.pdf]]
