2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Design Patterns]]

# Distance Strategy Pattern

The Strategy pattern packages a distance calculation as an interchangeable object. A clustering algorithm receives a Distance base pointer and calls its function operator without knowing whether the concrete measure is Euclidean, matching, mixed, or Mahalanobis.

Separating proximity from cluster control flow lets one algorithm be tested under several domain models. An algorithm that mathematically requires a particular distance should validate or construct that requirement instead of pretending every strategy is compatible.

# References

[[dataclusteringincplusplus.pdf]]

