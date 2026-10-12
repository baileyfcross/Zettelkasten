2026-09-28 03:43

Status: #baby

Tags: [[Genome Sequencing Acceleration]]

# KMP Hardware Accelerator

A KMP hardware accelerator implements prefix-guided pattern matching as a digital datapath. The source sequence streams through comparison logic, and the prefix table selects the next pattern state after a mismatch.

Parallel or pipelined instances can search multiple regions or patterns, but table storage and match reporting still consume resources. The book's prototype packages the KMP circuit as an IP core under host and DMA control.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

