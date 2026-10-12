2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Algorithm Framework]]

# Perform Clustering Hook

performClustering is a protected pure virtual const operation that contains or coordinates the method's numerical work. Every concrete Algorithm subclass must implement it, but external clients can reach it only through the public lifecycle.

The const declaration prevents modification of configured parameters while allowing explicitly mutable working state. The hook commonly delegates to initialization and iteration helpers rather than becoming one monolithic function.

# References

[[dataclusteringincplusplus.pdf]]

