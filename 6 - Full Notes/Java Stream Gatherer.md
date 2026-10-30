2026-10-30 15:57

Status: #baby

Tags: [[Java Streams and Functional Processing]]

# Java Stream Gatherer

In the book's Java 23 setting, the preview `gather` operation generalizes custom intermediate stream processing through a `Gatherer`. A gatherer can maintain state, integrate elements, emit zero or more results, combine parallel state when supported, and finish the transformation.

This allows transformations such as fixed or sliding windows and running scans that are awkward to express as independent map, filter, or reduce stages. Built-in gatherers cover common cases, while a custom gatherer must define its state and parallel semantics deliberately. Preview use requires the matching language flags and remains version-specific.

By Java 24, gatherers were finalized. The predefined family includes fixed and sliding windows, `fold`, `scan`, and virtual-thread-backed `mapConcurrent`; gatherers can also be composed. Custom implementations separate initialization, integration, optional parallel combination, and finishing, and the gather operation produces a reference stream rather than a primitive-stream specialization.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[java25andbeyond_modernjavamadeeasy.epub]]
