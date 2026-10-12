2026-09-27 00:11

Status: #baby

Tags: [[.NET Data Parallelism and PLINQ]]

# Parallel ForEach

`Parallel.ForEach` distributes elements or partitions of a source among workers and applies one delegate to them. It extends data-parallel loop execution beyond a simple numeric range and can accept custom partitioning and local-state functions.

The source's enumeration behavior and partitioner affect load balance. An unordered concurrent traversal should not be used when the algorithm requires sequential side effects or stable encounter order unless those requirements are restored explicitly.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
