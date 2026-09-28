2026-09-28 03:43

Status: #baby

Tags: [[Controllable Dataflow Processing]]

# General Dataflow Framework

A general dataflow framework represents computation as vertices connected by directed data dependencies. It can expose finer-grained scheduling than a fixed map-and-reduce pipeline and can express several execution patterns with one graph abstraction.

Generality alone does not ensure that the same application can change between batch, iterative, incremental, and streaming behavior. The [[Controllable Dataflow Model]] adds explicit semantics to the flows so execution policy can change without rewriting the computational cores.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

