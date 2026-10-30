2026-10-30 15:57

Status: #baby

Tags: [[Java Streams and Functional Processing]]

# Java Stream collect and reduce

`reduce` combines stream elements into one value using an identity and associative accumulator, making sums and other folds explicit. `collect` performs mutable reduction through a result supplier, accumulator, and combiner or through a predefined `Collector`, producing lists, maps, groups, and summaries.

Parallel execution depends on correct combination: the identity must be neutral and the reduction operation associative, while collector state must be partitionable or safely concurrent. A reduction describes one aggregate result; it should not use a shared external variable as an unofficial accumulator.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
