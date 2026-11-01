2026-10-31 22:04

Status: #baby

Tags: [[SIMD Numerical Accuracy and Statistics]]

# Vector-Length-Dependent Rounding

Vector-length-dependent rounding occurs when changing the number of lanes changes how input values are partitioned among partial floating-point accumulators. Each lane develops its own rounding history before a final reduction combines the partial results.

The algorithm can remain logically correct and vector-length agnostic while returning slightly different bits at 128, 256, and 512 bits. The book's mean and standard-deviation example shows this effect directly. A numerical contract should therefore specify tolerances or apply [[SIMD Kahan Summation|compensation]] rather than assume bitwise equality across species.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
