2026-10-31 22:04

Status: #baby

Tags: [[SIMD Reductions and Scan Algorithms]]

# Cross-Vector Scan Carry

A cross-vector scan carry propagates the completed accumulation from one vector block into the local scan of the next block. After scanning a prefix block, its last lane becomes the carry added to every lane of the following block; a suffix scan uses the corresponding first lane while moving backward.

This step converts independent local cumulative results into a continuous global sequence. It also introduces an inter-block dependency, so unrolling may compute several local scans independently before applying carries in order. [[SIMD Loop Unrolling]] uses that separation to expose instruction-level work.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
