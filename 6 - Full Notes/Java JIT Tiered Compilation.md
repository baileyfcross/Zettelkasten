2026-10-31 22:04

Status: #baby

Tags: [[Java SIMD Performance Engineering]]

# Java JIT Tiered Compilation

Java JIT tiered compilation moves hot code from interpreted bytecode through quickly compiled, profiling-oriented machine code and eventually to more aggressively optimized machine code when execution evidence justifies the compilation cost. The early tier gathers counters and branch behavior; the later tier can unroll loops and replace expensive operations.

In the book's divisibility loop, the early compiler retains integer division and profiling machinery, while the optimizing compiler replaces constant division with multiplication and shifts and unrolls iterations. [[JIT-Generated Assembly Inspection]] is needed to tell which tier and transformations a benchmark actually exercised.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
