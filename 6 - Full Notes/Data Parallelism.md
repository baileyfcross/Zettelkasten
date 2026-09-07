2026-09-06 22:42

Status: #baby

Tags: [[Parallel Neural Network Training]]

# Data Parallelism

Data parallelism gives multiple workers copies of a model and different subsets of the input. Each worker calculates partial results or gradients, which are then combined to keep the model replicas consistent.

The approach scales when example-level work dominates aggregation. Synchronization and communication can become bottlenecks as worker count grows or updates become more frequent.

# References

[[bigdatamanagementandprocessing.pdf]]
