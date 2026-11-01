2026-10-31 22:04

Status: #baby

Tags: [[SIMD Reductions and Scan Algorithms]]

# SIMD Vector Scan

A SIMD vector scan computes cumulative lane results by repeatedly shifting the current vector by powers of two and combining aligned values. A vector of width $W$ completes after $\log_2 W$ stages, and the final lane also contains the complete reduction.

The stage count is depth-optimal, yet each vector instruction performs work in lanes whose shifted partner is absent. Total element operations approach $W\log_2 W$, and every stage depends on the previous one. The scan can therefore be slower than a scalar recurrence while remaining essential inside more parallel algorithms.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
