2026-09-28 03:43

Status: #baby

Tags: [[FPGA Accelerator Co-Design]]

# Accelerator Locality Analysis

Accelerator locality analysis determines which values are reused closely enough to retain in on-chip memory. It examines access order, vector intersections, temporary results, and the cost of off-chip requests before buffer sizes and dataflows are fixed.

Locality can be more important than adding arithmetic units. A design that repeatedly fetches the same data may be bandwidth-bound even when its processing elements are mostly idle.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

