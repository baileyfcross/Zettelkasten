2026-09-06 00:13

Status: #baby

Tags: [[Search Algorithms]] · [[Java Arrays and Elementary Algorithms]]

# Binary Search

Binary search locates a target in ordered data by examining the middle item. A match ends the search; a smaller or larger middle value proves that one half cannot contain the target, so the algorithm continues only in the other half.

Repeated halving gives [[Logarithmic Time Complexity]], $O(\log n)$, and makes extremely large ordered collections searchable with few probes. The algorithm also reports failure when its [[Search Space]] becomes empty. Implementations must calculate the midpoint without causing [[Integer Overflow]].

The result need not be an exact match. A lower-bound variant returns the first position whose value is greater than or equal to a target, which supplies the insertion point that preserves sorted order. This generalizes binary search from finding an item to finding a boundary in a monotonic search space.

The same method can tune a game value when testing supplies “too high” or “too low” feedback. A designer brackets a [[Viable Balance Range]], tests its midpoint, discards the unsuitable half, and repeats. If no initial bounds are known, doubling or halving a provisional value until it crosses the desired behavior can establish the interval first.

# References

[[algorithms.epub]]
[[introductiontogamesystemdesign.pdf]]
[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
