2026-09-28 03:43

Status: #baby

Tags: [[Hybrid Last-Level Cache Design]]

# Shared STT-RAM Bank

A shared STT-RAM bank remains available across cores instead of being repeatedly reassigned to a single owner. Its high density makes it useful as common capacity when private allocations are insufficient.

Keeping some banks shared can avoid flushing data whenever the partition changes. The tradeoff is contention: a shared bank preserves contents across epochs but may receive requests from several cores.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

