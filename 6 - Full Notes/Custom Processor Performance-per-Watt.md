2026-09-28 03:43

Status: #baby

Tags: [[Stencil Processor Optimization]]

# Custom Processor Performance-per-Watt

Custom processor performance-per-watt measures useful application throughput against the power consumed by a deliberately simple, augmented core. A customized core may lose in absolute speed to a large CPU or GPU yet execute each unit of work with much less power.

The book's stencil design illustrates this tradeoff: a small core plus tiling, cache controls, SIMD, and DMA preserved programmability while approaching FPGA-like efficiency. Comparisons must still report workload, technology assumptions, and absolute performance, not efficiency alone.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

