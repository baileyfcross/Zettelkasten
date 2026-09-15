2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Algorithm Framework]]

# Preprocessing Hook in Clustering Algorithm

Algorithm-specific preprocessing prepares reusable structures before the main iteration, such as a distance matrix, random initial centers, hierarchy forest, covariance storage, or fuzzy membership matrix. ClusLib places such work inside the concrete computation or initialization helpers.

Separating preprocessing from repeated updates clarifies cost and state lifetime. Anything derived solely from input parameters must be rebuilt or invalidated when those parameters change.

# References

[[dataclusteringincplusplus.pdf]]

