2026-10-31 22:04

Status: #baby

Tags: [[SIMD Algorithm Reformulation Patterns]]

# SIMD Maximum Subarray Reformulation

SIMD maximum-subarray reformulation replaces Kadane's conditional restart recurrence with operations on prefix sums. If $P_j$ is the exclusive prefix sum at endpoint $j$, the best subarray ending there is $P_j-\min_{i<j}P_i$; a final maximum chooses the best endpoint.

The new form decomposes into an [[Inclusive and Exclusive Scan|exclusive sum scan]], a prefix-minimum scan, and a maximum reduction, all based on associative operators. These operations can be fused within vector blocks. The transformation is useful because it changes a history-dependent branch into bulk cumulative data, not because it changes the linear asymptotic complexity.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
