2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Dataset Modeling]]

# Gaussian Mixture Dataset Generator

DatasetGenerator is a DataAdapter that samples points from several multivariate Gaussian components. It receives component means, covariance matrices, desired record counts, and a random seed, then fills a standard numeric Dataset.

The seed makes generated experiments reproducible, while labels identify the generating component for later cross-tabulation. Using the same adapter interface as a file reader lets algorithms ignore whether records were loaded or simulated.

# References

[[dataclusteringincplusplus.pdf]]

