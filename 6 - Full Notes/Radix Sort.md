2026-09-06 00:13

Status: #baby

Tags: [[Sorting Algorithms]]

# Radix Sort

Radix sort orders records by distributing them according to successive parts of their keys. Beginning with the least significant digit or character, it places items into ordered buckets, collects the buckets without disturbing their internal order, and repeats for the next position.

For $n$ keys of width $w$, its complexity is $O(nw)$. Because it treats even numerical keys as sequences of symbols rather than comparing their complete values, it is a [[String Sorting]] method.

# References

[[algorithms.epub]]
