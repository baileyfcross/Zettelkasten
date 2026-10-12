2026-09-28 03:43

Status: #baby

Tags: [[Hybrid Last-Level Cache Design]]

# Per-Line Read and Write Counters

Per-line read and write counters summarize how a cache line is being used. Their ratio guides whether the line should remain in SRAM, move to STT-RAM, or make room for a line with a more suitable access pattern.

The counters introduce storage overhead and must be reset after migration or replacement. They are a compact approximation of behavior, so the threshold should reflect the relative read and write costs of the memory technologies.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

