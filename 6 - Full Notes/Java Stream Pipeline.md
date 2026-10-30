2026-10-30 15:57

Status: #baby

Tags: [[Java Streams and Functional Processing]]

# Java Stream Pipeline

A Java stream pipeline connects a source, zero or more intermediate operations, and a terminal operation. It describes aggregate processing over a sequence of elements without exposing the loop that advances through them.

Intermediate operations such as `filter` and `map` return another stream, while a terminal operation such as `collect`, `count`, or `forEach` produces a result or effect and consumes the pipeline. The source itself is not modified merely because a stream was created from it.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
