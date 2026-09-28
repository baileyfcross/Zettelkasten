2026-09-28 03:43

Status: #baby

Tags: [[Controllable Dataflow Processing]]

# Dataflow Control Primitive

A dataflow control primitive is metadata that changes how a flow participates in execution. The book's model distinguishes properties such as static versus streaming generation, persisted versus transient state, cached reuse, iteration boundaries, and immediate propagation.

These controls let identical execution functions participate in different runtime behaviors. They also make performance choices visible: persistence can support reuse, streaming can lower waiting time, and iteration or instant propagation determines when downstream work may start.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

