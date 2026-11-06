2026-09-06 00:13

Status: #baby

Tags: [[Sorting Algorithms]] [[Abstract Data Structures]]

# Quicksort

Quicksort chooses a [[Quicksort Pivot]], partitions the remaining items so smaller values lie on one side and the rest on the other, and repeats the operation within the resulting groups. Every completed partition puts the pivot in its final position and improves the relative placement of the other items.

Random pivot selection gives expected [[Loglinear Time Complexity]], $O(n\log n)$. Consistently extreme pivots can degrade performance toward quadratic time, but that pathological sequence is extraordinarily unlikely under effective randomization.

An in-place implementation partitions an array segment around its pivot, recursively sorts the two resulting segments, and stops when a segment has fewer than two elements. The partition step is linear in the current segment size; the recursion shape determines whether total work is near $O(n\log n)$ or the quadratic worst case.

Practical implementations reduce pathological recursion with randomized or median-of-three pivots and may recurse only into the smaller partition while iterating over the larger. The method has strong cache behavior and little auxiliary storage, but classical in-place partitioning lacks [[Sorting Stability]].

# References

[[algorithms.epub]]

[[statisticalcomputingincplusplusandr.pdf]]
[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
