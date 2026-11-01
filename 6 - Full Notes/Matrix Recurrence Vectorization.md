2026-10-31 22:04

Status: #baby

Tags: [[SIMD Algorithm Reformulation Patterns]]

# Matrix Recurrence Vectorization

Matrix recurrence vectorization rewrites a fixed-order scalar recurrence as repeated multiplication by a small transition matrix. Powers or prefix products of that matrix can advance several sequence positions together instead of following each dependency one step at a time.

The book applies the pattern to Fibonacci numbers and continued-fraction convergents. [[Structure of Arrays for SIMD]] stores corresponding matrix components in separate vectors, while a multiplication scan constructs several transition products. The transformation exposes parallel work but may still lose when the sequence is short or a simpler scalar leap skips unnecessary terms.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
