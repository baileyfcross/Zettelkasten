2026-09-28 03:43

Status: #baby

Tags: [[Controllable Dataflow Processing]]

# Controllable Dataflow Model

The controllable dataflow model separates application logic from execution behavior. User-defined execution cores form vertices, directed flows carry data among them, and a [[Dataflow Control Primitive]] states how each flow is generated, retained, scheduled, or iterated.

Changing those primitives can run the same label-propagation logic as iterative batch work, synchronized incremental work, or incremental stream processing. The model therefore makes execution semantics a configurable property of the flow instead of embedding them in separate application implementations.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

