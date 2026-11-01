2026-10-31 22:04

Status: #baby

Tags: [[Java SIMD Foundations and Hardware Portability]]

# Vector Lane

A vector lane is one fixed position in a hardware or API vector. A lane holds an element value, and a lane-wise operation applies the same operator independently at corresponding positions of its input vectors.

Lane count equals vector bit width divided by element bit width: a 128-bit vector has four 32-bit integer or floating-point lanes. The distinction between a lane and the value stored in it matters because masks activate positions, shuffles move values among positions, and [[Java Vector Species and Tail Processing|species]] determine how many positions a loop processes at once.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
