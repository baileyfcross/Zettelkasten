2026-10-31 22:04

Status: #baby

Tags: [[Java SIMD Performance Engineering]]

# SIMD Asymmetric Loop Scheduling

SIMD asymmetric loop scheduling interleaves different stages from independent data streams instead of placing identical operations from each stream side by side. A prologue starts one stream early, the loop overlaps its rearrangement with another stream's comparison or blend, and an epilogue completes the displaced stage.

The book applies this schedule to bitonic merging. The instructions are data-independent and also use different processor subsystems, reducing [[SIMD Structural Hazard|structural contention]] compared with a symmetric unroll. The source becomes less intuitive, so the schedule should be derived from dependencies and confirmed by generated code and benchmarks.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
