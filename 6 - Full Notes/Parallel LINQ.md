2026-09-08 21:16

Status: #baby

Tags: [[LINQ Query Construction]]

# Parallel LINQ

Parallel LINQ can partition an in-memory query across multiple workers by converting the source with `AsParallel`. It is intended for CPU-bound operations whose independent elements are expensive enough to outweigh partitioning and coordination overhead.

Parallel execution can change ordering and exposes unsafe shared state in query delegates. It should be adopted after measurement, with explicit ordering only when needed and with cancellation and exception behavior accounted for.

The design-patterns source places Parallel LINQ beside concurrent collections and task-based code. The comparison matters: PLINQ partitions a data query for CPU work, whereas `async`/`await` avoids tying up a thread while an operation waits. Applying both labels to a workload does not automatically improve its throughput.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
[[hands-ondesignpatternswithcandnetcore.pdf]]
