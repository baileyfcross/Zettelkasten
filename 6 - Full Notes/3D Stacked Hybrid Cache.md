2026-09-28 03:43

Status: #baby

Tags: [[Hybrid Last-Level Cache Design]]

# 3D Stacked Hybrid Cache

A 3D stacked hybrid cache places processor cores and cache banks on separate vertical layers connected by [[Through-Silicon Via]] links. The cache combines dense STT-RAM banks with SRAM or hybrid banks to balance capacity, leakage, write latency, and endurance.

Bank position matters because vertical and horizontal distance create nonuniform access latency. The architecture therefore couples memory technology with [[NUCA Cache Locality]] and [[Dynamic Hybrid Cache Partitioning]].

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

