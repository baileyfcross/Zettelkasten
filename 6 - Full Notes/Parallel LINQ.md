2026-09-08 21:16

Status: #baby

Tags: [[LINQ Query Construction]]

# Parallel LINQ

Parallel LINQ can partition an in-memory query across multiple workers by converting the source with `AsParallel`. It is intended for CPU-bound operations whose independent elements are expensive enough to outweigh partitioning and coordination overhead.

Parallel execution can change ordering and exposes unsafe shared state in query delegates. It should be adopted after measurement, with explicit ordering only when needed and with cancellation and exception behavior accounted for.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
