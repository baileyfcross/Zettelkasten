2026-09-28 03:43

Status: #baby

Tags: [[Hybrid Last-Level Cache Design]]

# SRAM Read-Aware Policy

An SRAM read-aware policy identifies lines whose read frequency substantially exceeds their write frequency and migrates them to STT-RAM. The move frees scarce SRAM space for write-heavy lines that benefit more from fast writes.

The book triggers this decision on a write hit so the migration can avoid an extra preliminary read. [[Per-Line Read and Write Counters]] supply the evidence for distinguishing read-dominant from write-dominant lines.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

