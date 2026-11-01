2026-10-31 22:04

Status: #baby

Tags: [[SIMD Numerical Accuracy and Statistics]]

# Kahan Compensated Summation

Kahan compensated summation maintains a running total and a correction for low-order information lost by each floating-point addition. After forming a tentative sum, arithmetic involving the old and new totals estimates the discarded contribution and carries it into later additions.

Compensation improves accuracy when values differ greatly in magnitude or many rounding steps accumulate. It also adds dependent arithmetic and is not free: the book finds large slowdowns on some processors even when modern out-of-order cores hide part of the extra work. Its use should follow an explicit error requirement.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
