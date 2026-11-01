2026-10-31 22:04

Status: #baby

Tags: [[SIMD Numerical Accuracy and Statistics]]

# Single-Pass Mean and Standard Deviation

A single-pass mean and standard-deviation kernel accumulates $S_1=\sum x_i$ and $S_2=\sum x_i^2$ together. It computes the mean as $S_1/N$ and the population variance as $S_2/N-(S_1/N)^2$, then takes the square root.

The method halves array traversal compared with [[Two-Pass Variance Algorithm|a centered two-pass calculation]] and maps naturally to two vector accumulators. Its final difference can suffer [[Catastrophic Cancellation]], and both long sums incur rounding. The book uses compensation or a double-precision reference to distinguish throughput improvement from adequate accuracy.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
