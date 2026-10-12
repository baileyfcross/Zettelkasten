2026-09-06 22:42

Status: #baby

Tags: [[Hardware Acceleration for Big Data]]

# Field-Programmable Gate Array

A field-programmable gate array is a reconfigurable device whose logic, memory blocks, and communication paths can be arranged for a particular computation. It supports specialized pipelines and fine-grained parallelism without manufacturing a fixed custom chip.

Design effort and compilation time are higher than ordinary software, which motivates [[High-Level Synthesis]].

In a heterogeneous accelerator, the FPGA's programmable logic usually works beside a host processor and DMA engine. The fabric implements parallel or pipelined hot code, while the processor retains operating-system services, control-heavy logic, and application orchestration.

# References

[[bigdatamanagementandprocessing.pdf]]

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]
