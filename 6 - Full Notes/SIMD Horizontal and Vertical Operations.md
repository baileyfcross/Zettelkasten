2026-10-31 22:04

Status: #baby

Tags: [[SIMD Reductions and Scan Algorithms]]

# SIMD Horizontal and Vertical Operations

Vertical SIMD operations act independently at corresponding lane positions, such as adding two vectors element by element. Horizontal operations exchange or combine values within a vector, including reductions, shuffles, permutations, and scans.

Vertical work maps directly to repeated arithmetic units and usually offers the cleanest throughput. Horizontal work requires cross-lane data paths, consumes more power and hardware area, and often has greater latency. The book's statistical kernel improves markedly when [[Java Vector Lane Reduction|lane reductions]] move outside the main loop.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
