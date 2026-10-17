2026-10-17 17:30

Status: #baby

Tags: [[Constraint-Preserving QAOA]]

# Ring and Complete-Graph XY Mixers

A complete-graph XY mixer couples every pair of positions in a one-hot register, while a ring mixer couples only neighboring positions with periodic closure. Both preserve Hamming weight and can connect all colors, but they impose different circuit depth and transition structure.

In the lecture's cited noiseless graph-coloring benchmarks, the simultaneous complete mixer generally achieved higher approximation ratios than the simultaneous ring mixer at shallow to medium QAOA depth, with the advantage narrowing as performance approached one. The result is problem- and implementation-specific rather than a universal ordering.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

