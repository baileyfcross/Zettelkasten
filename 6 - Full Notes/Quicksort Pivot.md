2026-09-06 00:13

Status: #baby

Tags: [[Sorting Algorithms]]

# Quicksort Pivot

A quicksort pivot is the item used to partition a collection during [[Quicksort]]. Items smaller than the pivot move to one side, while items at least as large move to the other, leaving the pivot in its final sorted position.

An extreme pivot such as the current minimum produces a badly unbalanced partition and little progress. Selecting pivots at random avoids spending extra work searching for an ideal pivot while making a long sequence of worst choices exceedingly improbable.

Median-of-three selection uses the median of the first, middle, and last candidates to encourage more balanced practical partitions. Pivot quality affects the height of the recursion tree: balanced splits keep it logarithmic, while repeatedly choosing an extreme produces a chain and quadratic total work.

# References

[[algorithms.epub]]
[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
