2026-09-06 00:13

Status: #baby

Tags: [[Search Algorithms]]

# Binary Search

Binary search locates a target in ordered data by examining the middle item. A match ends the search; a smaller or larger middle value proves that one half cannot contain the target, so the algorithm continues only in the other half.

Repeated halving gives [[Logarithmic Time Complexity]], $O(\log n)$, and makes extremely large ordered collections searchable with few probes. The algorithm also reports failure when its [[Search Space]] becomes empty. Implementations must calculate the midpoint without causing [[Integer Overflow]].

# References

[[algorithms.epub]]
