2026-09-14 22:06

Status: #baby

Tags: [[C++ Specialized Clustering Implementations]]

# Maximum-Likelihood Run Selection

A Gaussian-mixture example runs GMC from several random initial centers and retains the Results object with the greatest log-likelihood. It also calculates average likelihood and iteration count across the attempted starts.

Multiple starts address local maxima in the EM objective. A higher fitted likelihood under the same component model improves optimization but does not by itself select the correct number or covariance structure.

# References

[[dataclusteringincplusplus.pdf]]

