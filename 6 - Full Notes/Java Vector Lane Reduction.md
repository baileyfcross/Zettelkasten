2026-10-31 22:04

Status: #baby

Tags: [[SIMD Reductions and Scan Algorithms]]

# Java Vector Lane Reduction

A Java vector lane reduction combines every lane with an associative operator and returns one scalar, such as a sum, maximum, minimum, or XOR. It is a horizontal operation because information moves across lane boundaries.

Reduction is appropriate at the end of an accumulation but expensive when repeated for every input block. [[SIMD Partial-Accumulator Reduction]] keeps several lane-local totals during the loop and reduces only the final accumulator, lowering cross-lane work while changing the arithmetic grouping.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
