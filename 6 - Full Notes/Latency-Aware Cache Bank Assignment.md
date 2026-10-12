2026-09-28 03:43

Status: #baby

Tags: [[Hybrid Last-Level Cache Design]]

# Latency-Aware Cache Bank Assignment

Latency-aware cache bank assignment gives each core the unassigned SRAM or STT-RAM banks with the shortest access path after its bank quota is calculated. This adapts ordinary cache partitioning to a nonuniform three-dimensional layout.

A bank's technology and location are both relevant. Assigning capacity without distance can lower miss rate yet increase average access time, while choosing only nearby banks can ignore workload demand.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

