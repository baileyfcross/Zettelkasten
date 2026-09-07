2026-09-06 22:42

Status: #baby

Tags: [[Parallel Workload Resource Management]]

# Application Pack

An application pack is a group of parallel tasks scheduled to run concurrently on a fixed pool of processors. The pack finishes when its slowest member finishes, so processor assignments should reduce the maximum execution time rather than optimize each task independently.

Co-scheduling can partition a workload into several packs and execute those packs in sequence.

# References

[[bigdatamanagementandprocessing.pdf]]
