2026-09-14 21:34

Status: #baby

Tags: [[Network and Uncertain Data Clustering]]

# Kernighan-Lin Partitioning

Kernighan-Lin partitioning improves an initial balanced two-way graph division by considering paired vertex swaps. During a pass it selects swaps for their cumulative gain, locks moved vertices, and then keeps the best improving prefix.

Allowing temporary negative-gain moves helps escape some local traps that greedy improvement cannot cross. The result remains dependent on initialization and is commonly embedded in multilevel or repeated schemes.

# References

[[dataclustering.pdf]]

