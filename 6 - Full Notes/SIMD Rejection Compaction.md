2026-10-31 22:04

Status: #baby

Tags: [[SIMD Algorithm Reformulation Patterns]]

# SIMD Rejection Compaction

SIMD rejection compaction evaluates a batch of candidates, marks acceptable lanes, and uses [[Java Vector Compress Operation|compress]] to pack accepted results into the next contiguous output positions. The loop advances by the mask's true count rather than by the original batch width.

The book applies this pattern to bounded integers from a [[Linear Congruential Generator]]. Values that would create modular bias are rejected, but no lane-specific retry loop is required; accepted remainders are compacted and later batches fill the remaining output. Performance depends on both rejection rate and native compress support.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
