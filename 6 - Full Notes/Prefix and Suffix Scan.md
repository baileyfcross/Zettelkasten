2026-10-31 22:04

Status: #baby

Tags: [[SIMD Reductions and Scan Algorithms]]

# Prefix and Suffix Scan

A prefix scan accumulates from the start of a sequence toward each position, whereas a suffix scan accumulates from the end backward. Both are cumulative operations and may be inclusive or exclusive.

Their algebra is symmetric, but implementations can differ at boundaries and in memory behavior. The book handles a short suffix tail before entering the full-vector loop and observes modest hardware-dependent differences between forward and backward traversal. [[Cross-Vector Scan Carry]] connects the local scans from adjacent blocks.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
