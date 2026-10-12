2026-09-28 03:43

Status: #baby

Tags: [[Controllable Dataflow Processing]]

# Active Working Set

An active working set contains the records or graph vertices changed by the preceding incremental step. Each iteration processes that set, propagates its effects, and constructs the next set from newly affected records.

When the set becomes empty, the computation has reached a fixed point. Ordering the set by priority can accelerate convergence, but the priority changes scheduling rather than the correctness condition that every relevant update must eventually be processed.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

