2026-10-31 22:04

Status: #baby

Tags: [[Java SIMD Performance Engineering]]

# SIMD Register Pressure

SIMD register pressure is the demand created by simultaneously live vector values, masks, indices, and temporaries. When the demand exceeds the physical registers available to compiled code, values spill to memory and later reload, adding traffic and dependencies.

Wide transpositions and aggressive [[SIMD Loop Unrolling|unrolling]] raise pressure quickly. In the book's scan benchmarks, a sixteen-vector pivot can lose despite reducing arithmetic work, while a simpler fixed-width version performs better. Register capacity is therefore part of the algorithm budget, not merely a compiler implementation detail.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
