2026-09-28 03:43

Status: #baby

Tags: [[Controllable Dataflow Processing]]

# Sparse Computational Dependency

A sparse computational dependency exists when a change affects only a small portion of the next computation. In iterative graph algorithms, fewer vertex labels may change as convergence approaches, so reprocessing every vertex wastes work.

An incremental runtime exploits this sparsity by forwarding unchanged values and activating only dependent tasks. The benefit depends on representing causality precisely enough that the runtime can build an [[Active Working Set]] without omitting necessary updates.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

