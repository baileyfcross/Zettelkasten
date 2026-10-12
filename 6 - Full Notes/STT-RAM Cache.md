2026-09-28 03:43

Status: #baby

Tags: [[Hybrid Last-Level Cache Design]]

# STT-RAM Cache

An STT-RAM cache uses spin-transfer-torque magnetic memory cells for cache storage. Compared with SRAM, it offers higher density and much lower leakage, which can enlarge a last-level cache without the static-energy cost of an equally sized SRAM design.

Its writes are slower, consume more energy, and have finite endurance. A practical design therefore combines STT-RAM capacity with faster SRAM regions and applies [[STT-RAM Write-Aware Policy]] and [[STT-RAM Endurance Management]].

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

