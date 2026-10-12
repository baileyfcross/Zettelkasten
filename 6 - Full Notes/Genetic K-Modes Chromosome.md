2026-09-14 22:06

Status: #baby

Tags: [[C++ Specialized Clustering Implementations]]

# Genetic K-Modes Chromosome

The genetic K-modes implementation represents a categorical clustering candidate as a chromosome encoding cluster modes or the assignments from which those modes are derived. A population contains several candidates explored concurrently across generations.

The encoding must support efficient distance evaluation and preserve valid categorical values. Initialization diversity gives the search access to alternatives that a single greedy K-modes run might miss.

# References

[[dataclusteringincplusplus.pdf]]

