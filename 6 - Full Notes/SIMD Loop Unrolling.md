2026-10-31 22:04

Status: #baby

Tags: [[Java SIMD Performance Engineering]]

# SIMD Loop Unrolling

SIMD loop unrolling processes several vector blocks in one loop body. It reduces branch and index overhead and creates independent instruction streams that a superscalar processor can schedule around [[SIMD Dependency Chain|dependency latency]].

The unroll factor is constrained by code size and [[SIMD Register Pressure]]. The book often tests factors of four, eight, or sixteen and finds that benefits vary by microarchitecture. More copies can worsen performance when live vectors spill to memory or when all copies compete for the same execution unit.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
