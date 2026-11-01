2026-10-31 22:04

Status: #baby

Tags: [[SIMD Reductions and Scan Algorithms]]

# Associative Operation Requirement for Scan

A parallel scan requires an associative combine operation: regrouping values must not change the mathematical result. The tree may evaluate $(a\mathbin\oplus b)\mathbin\oplus(c\mathbin\oplus d)$ instead of the scalar nesting, so both groupings must be equivalent under the intended algebra.

Addition, multiplication, minimum, maximum, and XOR satisfy the structural requirement, enabling prefix sums, products, extrema, and bitwise folds. Finite floating-point addition is not exactly associative, so a scan remains an implementation of a chosen rounding order rather than an assurance of bitwise equality with sequential accumulation.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
