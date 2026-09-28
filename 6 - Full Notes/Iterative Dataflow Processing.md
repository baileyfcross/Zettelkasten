2026-09-28 03:43

Status: #baby

Tags: [[Controllable Dataflow Processing]]

# Iterative Dataflow Processing

Iterative dataflow processing runs a computation in rounds, with each round consuming results from an earlier round. Caching or buffering intermediate state avoids rebuilding the entire working set from persistent storage on every iteration.

The remaining difficulty is dependency granularity. A framework can reuse the preceding result yet still recompute unchanged regions unless it represents which tasks were actually affected. [[Sparse Computational Dependency]] and [[Active Working Set]] make that distinction explicit.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

