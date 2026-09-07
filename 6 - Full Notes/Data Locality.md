2026-09-06 22:42

Status: #baby

Tags: [[Parallel Workload Resource Management]]

# Data Locality

Data locality places computation on or near the machine that stores its input. In MapReduce systems, a local map task reads from a worker's disk instead of consuming cluster-network bandwidth.

Waiting indefinitely for a local slot can delay completion, so a scheduler balances locality against queue time, fairness, deadlines, and the distribution of replicas.

# References

[[bigdatamanagementandprocessing.pdf]]
