2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Distance Framework]]

# Minkowski Distance Functor

MinkowskiDistance derives from Distance and evaluates the p-norm of component differences for numeric records. Its parameter p selects a family that includes Manhattan distance at one and Euclidean distance at two.

The implementation validates compatible numeric schemas and accumulates powered component differences before applying the reciprocal exponent. Larger p values increasingly emphasize the greatest coordinate difference.

# References

[[dataclusteringincplusplus.pdf]]

