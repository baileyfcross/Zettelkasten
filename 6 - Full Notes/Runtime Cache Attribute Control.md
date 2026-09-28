2026-09-28 03:43

Status: #baby

Tags: [[Stencil Processor Optimization]]

# Runtime Cache Attribute Control

Runtime cache attribute control changes how a selected address range uses the cache while the rest of memory keeps its normal policy. It allows software to express that a region will be overwritten completely or should bypass an allocation behavior that would only fetch useless old data.

This control is more selective than disabling caching globally. The book applies it through a [[No-Allocate Store Policy]], reducing memory traffic with little added hardware cost.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

