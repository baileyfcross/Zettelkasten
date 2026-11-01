2026-10-31 22:04

Status: #baby

Tags: [[Java SIMD Performance Engineering]]

# SIMD Dependency Chain

A SIMD dependency chain is a sequence in which each vector instruction needs the result of its immediate predecessor. The processor cannot execute later operations early, so the chain's latency becomes the critical path even when each instruction updates many lanes.

Sequential accumulation and the stages of a vector scan create such chains. [[Pairwise Vector Summation]] shortens one by building a tree, and [[SIMD Loop Unrolling]] can interleave independent chains from several blocks. Unrolling does not remove dependencies inside each chain; it only offers other work while one result is pending.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
