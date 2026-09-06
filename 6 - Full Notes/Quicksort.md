2026-09-06 00:13

Status: #baby

Tags: [[Sorting Algorithms]]

# Quicksort

Quicksort chooses a [[Quicksort Pivot]], partitions the remaining items so smaller values lie on one side and the rest on the other, and repeats the operation within the resulting groups. Every completed partition puts the pivot in its final position and improves the relative placement of the other items.

Random pivot selection gives expected [[Loglinear Time Complexity]], $O(n\log n)$. Consistently extreme pivots can degrade performance toward quadratic time, but that pathological sequence is extraordinarily unlikely under effective randomization.

# References

[[algorithms.epub]]
