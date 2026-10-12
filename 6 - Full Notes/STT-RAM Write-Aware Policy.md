2026-09-28 03:43

Status: #baby

Tags: [[Hybrid Last-Level Cache Design]]

# STT-RAM Write-Aware Policy

An STT-RAM write-aware policy redirects a write that would hit or enter STT-RAM toward SRAM when space or a suitable victim is available. This shifts expensive writes away from the slower, endurance-limited region.

Migration may require evicting or relocating an SRAM line, so the policy uses access counters and replacement state rather than moving every written line blindly. It works with [[SRAM Read-Aware Policy]] to reserve STT-RAM for read-dominant data.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

