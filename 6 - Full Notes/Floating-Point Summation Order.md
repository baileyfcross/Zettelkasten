2026-10-31 22:04

Status: #baby

Tags: [[SIMD Numerical Accuracy and Statistics]]

# Floating-Point Summation Order

Floating-point summation order determines which rounded intermediate values feed later additions. Because finite-precision addition is not associative, a left-to-right chain, a pairwise tree, and lane-local partial accumulators can return different representable numbers for the same mathematical sum.

The difference is not by itself evidence that one implementation is defective. Accuracy must be checked against a suitable reference and tolerance. [[Pairwise Vector Summation]] can shorten dependencies, while [[Kahan Compensated Summation]] explicitly tracks lost low-order information when the application requires greater stability.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
