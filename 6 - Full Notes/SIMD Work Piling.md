2026-10-31 22:04

Status: #baby

Tags: [[SIMD Algorithm Reformulation Patterns]]

# SIMD Work Piling

SIMD work piling assigns a new task to a lane as soon as that lane's previous task finishes, instead of waiting for every lane in the vector to complete. A completion mask identifies holes, and [[Java Vector Expand Operation|expand]] places packed new inputs into those positions.

The technique improves lane occupancy for [[SIMD Divergent Lane Execution|divergent workloads]] but complicates state tracking and output placement. In the Collatz study, combining work piling with memoization required additional gather, scatter, compress, and expand operations; the extra memory traffic made it slower than straightforward memoization despite higher lane utilization.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
