2026-09-06 22:42

Status: #baby

Tags: [[Hardware Acceleration for Big Data]]

# Graph Workload Irregularity

Graph workload irregularity comes from nonuniform degrees, pointer-like adjacency access, data-dependent traversal, and changing active vertex sets. Consecutive operations may touch unrelated memory and perform very different amounts of work.

These properties weaken caching, vectorization, predictable pipelines, and static load balance, making graph analytics difficult for both general and specialized hardware.

# References

[[bigdatamanagementandprocessing.pdf]]
