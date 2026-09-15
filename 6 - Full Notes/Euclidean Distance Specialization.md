2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Distance Framework]]

# Euclidean Distance Specialization

EuclideanDistance specializes Minkowski behavior for p equal to two, the common straight-line metric used by center-based clustering. A dedicated class gives clients a meaningful type without repeatedly supplying the exponent.

The specialization can reuse the general implementation while communicating an algorithm's expected geometry. Its result remains scale-sensitive, so numeric preprocessing must be decided outside the distance call.

# References

[[dataclusteringincplusplus.pdf]]

