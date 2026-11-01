2026-10-31 22:04

Status: #baby

Tags: [[SIMD Reductions and Scan Algorithms]]

# SIMD Transposed Scan

A SIMD transposed scan pivots several consecutive vectors so equal lane positions from different blocks become one vector. A scan tree then operates vertically across those blocks, using every lane for independent instances of the same combine step.

The method supports [[Blelloch Work-Optimal Scan|work-optimal scans]] and adds instruction-level independence, but it requires [[Java Vector Zip and Unzip Transposition|zip and unzip permutations]] before and often after the scan. Large pivots can increase register pressure or spill to memory, so shorter fixed-width variants may outperform more general transpositions.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
