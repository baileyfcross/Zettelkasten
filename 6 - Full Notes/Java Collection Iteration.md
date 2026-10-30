2026-10-30 15:57

Status: #baby

Tags: [[Java Collections and Date-Time]]

# Java Collection Iteration

`Iterable<T>` supplies an `Iterator<T>`, allowing a collection to expose elements one at a time without revealing its storage. The enhanced-for statement uses this protocol, while an iterator provides explicit `hasNext`, `next`, and supported removal behavior.

Iteration order belongs to the concrete collection's contract: a list has encounter order, a sorted collection has comparison order, and a hash collection does not promise a useful stable order. Structural modification outside the iterator during traversal can be detected as concurrent modification rather than silently producing an inconsistent walk.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
