2026-10-31 22:04

Status: #baby

Tags: [[Java SIMD Performance Engineering]]

# SIMD Over-Optimization

SIMD over-optimization occurs when machinery added to remove one inefficiency creates a larger cost elsewhere. Improving lane occupancy, reducing arithmetic, or eliminating a shuffle is not useful when the change adds more expensive memory accesses, register spills, or control bookkeeping.

The book's strongest example combines [[SIMD Memoized Irregular Workload|memoization]] with [[SIMD Work Piling]]. Compressing active lanes and refilling holes improves utilization, but repeated gather and scatter operations multiply memory traffic and make the comprehensive version slower than simple memoization. Each optimization should therefore be evaluated in the complete kernel, not by its local metric alone.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
