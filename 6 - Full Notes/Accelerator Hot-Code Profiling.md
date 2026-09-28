2026-09-28 03:43

Status: #baby

Tags: [[FPGA Accelerator Co-Design]]

# Accelerator Hot-Code Profiling

Accelerator hot-code profiling measures where an application spends time and resources before selecting a hardware target. Instrumentation or profiling tools identify candidate regions whose execution cost is large enough to justify transfer and circuit overhead.

A hot region is not automatically suitable for an FPGA. Its control structure, parallelism, numerical operations, data volume, and dependencies must also admit an efficient hardware mapping.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

