2026-09-28 03:43

Status: #baby

Tags: [[Hybrid Last-Level Cache Design]]

# Cache Access-Aware Placement

Cache access-aware placement moves data between SRAM and STT-RAM according to observed reads and writes. Write-intensive lines favor SRAM because its writes are faster and cheaper; read-intensive lines can occupy the denser STT-RAM region.

The policy coordinates a [[STT-RAM Write-Aware Policy]] with a [[SRAM Read-Aware Policy]]. Its purpose is not simply to maximize hits, but to reduce write latency, energy, and wear while preserving useful capacity.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

