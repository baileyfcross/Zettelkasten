2026-09-28 03:43

Status: #baby

Tags: [[Controllable Dataflow Processing]]

# Batch Dataflow Processing

Batch dataflow processing executes a fixed computation over a static, persistent data set. Functions are arranged as a [[Dataflow Graph]], and the runtime distributes and schedules the resulting tasks across the cluster.

Its simple abstraction works well when the input is fully available before execution. It becomes inefficient when an application repeatedly reloads intermediate results, depends on several iterations, or needs to react continuously to new records; those needs motivate [[Iterative Dataflow Processing]], [[Incremental Dataflow Processing]], and [[Streaming Dataflow Processing]].

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

