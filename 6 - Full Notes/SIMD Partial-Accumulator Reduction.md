2026-10-31 22:04

Status: #baby

Tags: [[SIMD Reductions and Scan Algorithms]]

# SIMD Partial-Accumulator Reduction

SIMD partial-accumulator reduction maintains one running total per lane while traversing an array. Every loaded vector updates the accumulator lane-wise, and one horizontal reduction combines the lane totals after the loop.

This structure replaces a reduction per iteration with one final reduction and exposes regular arithmetic. It is effective for sums, sums of squares, maxima, and bitwise folds. Because each lane accumulates a different subsequence, it also changes floating-point evaluation order and can produce [[Vector-Length-Dependent Rounding]].

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
