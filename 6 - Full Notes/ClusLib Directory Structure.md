2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Build and Testing]]

# ClusLib Directory Structure

ClusLib organizes its highest-level tree into library code, configuration support, examples, macro files, and a test suite. The library directory is subdivided by responsibility into algorithms, clusters, datasets, distances, patterns, and utilities.

Keeping headers and source files for one subject together makes the design topology visible in the filesystem. Separate example directories give each algorithm an executable client without mixing demonstration code into reusable components.

# References

[[dataclusteringincplusplus.pdf]]

