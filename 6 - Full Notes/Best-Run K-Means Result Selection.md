2026-09-14 22:06

Status: #baby

Tags: [[C++ Partitional and Fuzzy Clustering]]

# Best-Run K-Means Result Selection

Best-run selection retains the Results object from the K-means run with the smallest error while also accumulating average error and iteration counts across all runs. The saved result is replaced whenever a lower objective is observed.

The lowest training objective is not automatically the most meaningful clustering, but it distinguishes better and worse local optima under the same model. Stability and domain evaluation remain separate checks.

# References

[[dataclusteringincplusplus.pdf]]

