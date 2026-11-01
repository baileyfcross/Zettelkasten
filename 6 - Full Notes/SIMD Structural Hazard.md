2026-10-31 22:04

Status: #baby

Tags: [[Java SIMD Performance Engineering]]

# SIMD Structural Hazard

A SIMD structural hazard occurs when independent instructions need the same limited execution resource at the same time. Their data have no dependency, but the core still serializes them because only a bounded number of shuffle, multiply, load, or other units can accept the operation.

Symmetrically unrolling identical vector work can expose this bottleneck: every stream reaches the same instruction class together. [[SIMD Asymmetric Loop Scheduling]] instead alternates dissimilar operations so out-of-order execution has a better chance of using separate subsystems concurrently.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
