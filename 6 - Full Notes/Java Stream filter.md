2026-10-30 15:57

Status: #baby

Tags: [[Java Streams and Functional Processing]]

# Java Stream filter

`Stream.filter` is an intermediate operation that retains elements for which a supplied `Predicate<T>` returns true. It preserves the element type and, for an ordered stream, the encounter order of retained values.

Because filtering is lazy, the predicate runs only as downstream demand reaches an element. A stateless predicate makes sequential and parallel behavior easier to reason about. Selection does not mutate the source; a terminal operation decides whether the retained elements become an array, collection, count, match, or effect.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
