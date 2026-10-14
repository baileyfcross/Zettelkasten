2026-09-06 22:42

Status: #baby

Tags: [[Hardware Acceleration for Big Data]]

# Graphics Processing Unit

A graphics processing unit provides many parallel execution units optimized for applying similar operations across large collections of data. High arithmetic throughput and bandwidth make it effective for regular numerical kernels.

Irregular graph workloads can underuse the device when branches diverge, memory references lack locality, or work is unevenly distributed among threads.

Neural-network and recommendation workloads show the other side of the tradeoff: regular dense operations can exploit the GPU's threads and bandwidth, yet transfer cost and runtime power remain substantial. Compression and sparsity can also turn a formerly regular network into an irregular workload better matched by configurable logic.

In an accelerated AI server, the GPU complements rather than replaces the CPU and DPU. The CPU coordinates control-oriented work, the GPU executes parallel tensor operations, and a [[Data Processing Unit]] can offload network, storage, security, and telemetry functions; storage and interconnect bottlenecks can still leave the accelerator idle.

# References

[[bigdatamanagementandprocessing.pdf]]

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

[[nvidiagpuinfrastructurefundamentals.pdf]]
