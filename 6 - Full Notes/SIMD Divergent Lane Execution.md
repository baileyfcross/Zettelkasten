2026-10-31 22:04

Status: #baby

Tags: [[SIMD Algorithm Reformulation Patterns]]

# SIMD Divergent Lane Execution

SIMD divergent lane execution occurs when inputs assigned to one vector need different control-flow paths or iteration counts. The hardware still advances the vector as one instruction stream, so completed lanes may sit inactive while the slowest lane continues.

The book's Collatz orbits are a clear example: neighboring starting values can require very different numbers of steps. [[SIMD Branchless Conditional Execution]] handles per-step branches with masks, while [[SIMD Work Piling]] tries to refill lanes that finish early. Both add work that must be compared with the utilization they recover.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
