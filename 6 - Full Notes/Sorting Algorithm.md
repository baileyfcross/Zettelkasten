2026-09-06 00:13

Status: #baby

Tags: [[Sorting Algorithms]]

# Sorting Algorithm

A sorting algorithm rearranges a collection of [[Data Record|records]] into an order determined by a [[Sort Key]]. Its output must be a [[Permutation]] of the input: every original record is retained, with only the order changed.

Different algorithms offer different advantages. [[Insertion Sort]] accepts streamed input, [[Radix Sort]] distributes records by key parts, [[Quicksort]] is fast in typical in-memory use, and [[Merge Sort]] supports systematic division and parallel work.

Selection also depends on [[Sorting Stability]], auxiliary memory, input shape, data location, and required predictability. Java's standard library reflects those trade-offs by using different hybrid strategies for primitive arrays and object arrays instead of one universal sorting method.

# References

[[algorithms.epub]]
[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
