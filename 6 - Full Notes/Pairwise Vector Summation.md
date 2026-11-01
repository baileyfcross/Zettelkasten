2026-10-31 22:04

Status: #baby

Tags: [[SIMD Numerical Accuracy and Statistics]]

# Pairwise Vector Summation

Pairwise vector summation combines independent input pairs and then merges their partial results as a tree instead of extending one long accumulator chain. The first-level additions can execute concurrently, shortening the critical dependency depth and improving [[Instruction-Level Parallelism]].

The tree also changes rounding. Intermediate magnitudes may remain smaller than in left-to-right accumulation, so more low-order contributions can survive, but the method does not eliminate error. The book's five-vector example produces different lane results under sequential and pairwise order even though the real-number sums are identical.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
