2026-10-31 22:04

Status: #baby

Tags: [[SIMD Algorithm Reformulation Patterns]]

# SIMD Residue-Class Lookahead

SIMD residue-class lookahead partitions integer states by their remainder modulo a power of two and precomputes several deterministic transition steps for each class. A state $n=2^k x+y$ is replaced by an affine result $Ax+B$ and a step-count increment selected from the table for $y$.

The Collatz implementation uses low trailing bits to choose coefficients through register-resident lane selection, replacing several unpredictable iterations with one multiply-add. Larger tables can look farther ahead but consume more vector storage and require special handling when a formula crosses the terminal state earlier than its general class derivation assumes.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
