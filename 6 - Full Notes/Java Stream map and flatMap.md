2026-10-30 15:57

Status: #baby

Tags: [[Java Streams and Functional Processing]]

# Java Stream map and flatMap

`map` applies a function to each stream element and emits one transformed result, potentially changing the element type. Primitive mapping variants avoid wrappers when the result is numeric.

`flatMap` applies a function that returns a stream for each input and then concatenates those nested streams into one output stream. It is appropriate for one-to-many structure such as lines to words or albums to songs. Both operations should describe transformation rather than mutate shared external state.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
