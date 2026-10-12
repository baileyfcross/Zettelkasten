2026-09-27 00:11

Status: #baby

Tags: [[.NET Data Parallelism and PLINQ]]

# PLINQ Ordering

PLINQ normally favors parallel throughput over preserving a source's encounter order. `AsOrdered` requests order-sensitive results, and `AsUnordered` can remove that requirement after the portion of a query that depends on it.

Ordering constrains how partitions are merged and may delay results while earlier elements finish. A query should preserve order only when it contributes to its meaning, because requesting it for convenience can erase much of the benefit of parallel execution.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
