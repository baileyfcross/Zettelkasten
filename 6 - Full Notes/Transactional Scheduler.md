2026-09-06 22:42

Status: #baby

Tags: [[In-Memory Data Processing]]

# Transactional Scheduler

A transactional scheduler orders or delays transactions to reduce conflicts before the concurrency-control mechanism forces aborts. Reactive scheduling learns from observed collisions, while dependency-aware scheduling can use known relationships between abstract operations and data objects.

The scheduler trades some immediate parallelism for less wasted work and higher committed throughput.

# References

[[bigdatamanagementandprocessing.pdf]]
