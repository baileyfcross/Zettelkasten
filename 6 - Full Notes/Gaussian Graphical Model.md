2026-09-29 19:17

Status: #baby

Tags: [[High-Dimensional Graphical Models]]

# Gaussian Graphical Model

A Gaussian graphical model represents the conditional dependencies among jointly Gaussian variables with an undirected graph. An edge joins two variables exactly when the corresponding off-diagonal entry of the precision matrix is nonzero.

This correspondence turns graph learning into structured estimation of an inverse covariance matrix or a collection of conditional regressions. It can remain feasible when variables outnumber observations if the graph degree is sufficiently small. In that regime, exact edge recovery is demanding, so prediction guarantees and partial graph recovery may be more realistic goals.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
