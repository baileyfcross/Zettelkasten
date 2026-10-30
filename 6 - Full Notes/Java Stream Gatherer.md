2026-10-30 15:57

Status: #baby

Tags: [[Java Streams and Functional Processing]]

# Java Stream Gatherer

In the book's Java 23 setting, the preview `gather` operation generalizes custom intermediate stream processing through a `Gatherer`. A gatherer can maintain state, integrate elements, emit zero or more results, combine parallel state when supported, and finish the transformation.

This allows transformations such as fixed or sliding windows and running scans that are awkward to express as independent map, filter, or reduce stages. Built-in gatherers cover common cases, while a custom gatherer must define its state and parallel semantics deliberately. Preview use requires the matching language flags and remains version-specific.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
