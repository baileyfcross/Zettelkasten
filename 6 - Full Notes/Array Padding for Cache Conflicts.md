2026-09-28 03:43

Status: #baby

Tags: [[Stencil Processor Optimization]]

# Array Padding for Cache Conflicts

Array padding changes an array dimension or layout so repeatedly accessed elements do not map to the same small set of cache locations. In a stencil, an unfortunate stride can create conflict misses even when the total working set should fit.

Padding must be chosen with the cache geometry and [[Loop Tiling for Stencil Locality]] in mind. It is therefore a hardware-software co-design decision: the software layout and the configurable cache determine the result together.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

