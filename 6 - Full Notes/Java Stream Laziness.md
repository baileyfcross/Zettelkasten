2026-10-30 15:57

Status: #baby

Tags: [[Java Streams and Functional Processing]]

# Java Stream Laziness

Java stream intermediate operations are lazy: they assemble a pipeline but do not pull source elements until a terminal operation requests a result. Elements can then flow through the composed stages one at a time rather than each stage materializing a complete temporary collection.

Laziness enables short-circuiting. A search or limited traversal can stop after enough elements are found, so later source values and their transformations are never evaluated. Side effects inside intermediate operations are therefore unreliable as independent work because no terminal consumption means no execution.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
