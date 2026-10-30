2026-10-30 15:57

Status: #baby

Tags: [[Java Streams and Functional Processing]]

# Java Primitive Stream Specializations

`IntStream`, `LongStream`, and `DoubleStream` specialize Java streams for primitive numeric values. They avoid wrapping every element and add numeric terminal operations such as `sum`, `average`, and range-oriented construction.

Mapping operations convert between object streams and primitive streams when a pipeline crosses that boundary. These interfaces extend the common base stream contract and remain single-use, closeable pipelines; specialization changes representation and available operations rather than the source-to-terminal processing model.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
