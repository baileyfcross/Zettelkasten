2026-09-28 03:43

Status: #baby

Tags: [[FPGA Accelerator Co-Design]]

# Algorithm-to-Hardware Task Partitioning

Algorithm-to-hardware task partitioning assigns the regular, compute-intensive, and parallel regions of an application to logic while retaining flexible control and remaining computation on the processor. It follows profiling and precedes detailed circuit design.

The boundary determines communication volume. Moving a small kernel that requires the entire dataset to cross the bus repeatedly may be worse than leaving it in software or enlarging the hardware region.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

