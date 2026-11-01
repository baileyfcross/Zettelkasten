2026-10-31 22:04

Status: #baby

Tags: [[SIMD Reductions and Scan Algorithms]]

# Inclusive and Exclusive Scan

An inclusive scan includes the current element in each cumulative result, while an exclusive scan reports the accumulation of preceding elements only. For input `[1,2,3,4]`, inclusive addition yields `[1,3,6,10]` and exclusive addition yields `[0,1,3,6]`.

The distinction affects reformulations. The maximum-subarray identity uses an exclusive prefix sum so each endpoint is compared with an earlier prefix minimum, while many cumulative totals use the inclusive form. A shift or a change in update order can convert between the two when the operator has an identity element.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
