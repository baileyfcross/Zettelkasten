2026-09-28 03:43

Status: #baby

Tags: [[Hybrid Last-Level Cache Design]]

# NUCA Cache Locality

NUCA cache locality recognizes that banks in a large shared cache have nonuniform access times. A core reaches nearby banks faster than distant banks, and three-dimensional stacking adds layer-dependent paths to the distance.

Allocation should therefore consider both capacity demand and physical latency. [[Latency-Aware Cache Bank Assignment]] gives a core low-latency banks after deciding how many SRAM and STT-RAM banks it should receive.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

