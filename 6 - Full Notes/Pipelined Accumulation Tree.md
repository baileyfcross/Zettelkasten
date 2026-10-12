2026-09-28 03:43

Status: #baby

Tags: [[FPGA Accelerator Co-Design]]

# Pipelined Accumulation Tree

A pipelined accumulation tree combines many partial values through successive layers of adders. Registering the layers raises throughput because new vector elements can enter before the preceding reduction has fully completed.

Tree width should reflect available processing elements and vector length. When a vector exceeds the lane count, the accelerator reduces fragments and accumulates their partial sums across multiple passes.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

