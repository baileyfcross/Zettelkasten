2026-09-28 03:43

Status: #baby

Tags: [[Hybrid Last-Level Cache Design]]

# Dynamic Hybrid Cache Partitioning

Dynamic hybrid cache partitioning periodically assigns shared SRAM and STT-RAM banks among processor cores from observed access behavior. It accounts for unequal write demand, miss behavior, and the different physical latencies of banks in a 3D stack.

The allocation has two parts: estimate how many banks of each technology a core needs, then choose nearby banks through [[Latency-Aware Cache Bank Assignment]]. Some [[Shared STT-RAM Bank]] capacity can remain common to reduce disruptive reassignment.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

