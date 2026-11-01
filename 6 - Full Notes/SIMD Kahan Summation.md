2026-10-31 22:04

Status: #baby

Tags: [[SIMD Numerical Accuracy and Statistics]]

# SIMD Kahan Summation

SIMD Kahan summation keeps a sum vector and a correction vector, applying [[Kahan Compensated Summation|compensation]] independently in every lane. After all blocks are processed, the corrected lane totals are combined with a horizontal reduction.

The approach stabilizes partial sums whose number and membership change with vector width, but it introduces several additional lane-wise operations and dependency chains. The book's ARM benchmarks show that a mathematically attractive compensated vector kernel can be much slower when the compiler or pipeline does not schedule those chains effectively.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
