2026-09-14 21:34

Status: #baby

Tags: [[Unsupervised Feature Selection for Clustering]] · [[Spectral Feature Scoring and Graph Structure]]

# Spectral Feature Selection

Spectral feature selection evaluates attributes by how well they preserve the structure encoded in a similarity graph. Eigenvectors of a graph operator provide soft indicators of important geometric or cluster relationships, and features are scored against those indicators.

The approach can detect nonlinear structure that a global variance score misses. Its conclusions depend on how the graph, edge weights, neighborhood scale, and number of spectral components are chosen.

The framework can represent supervised, unsupervised, and semi-supervised targets through different [[Sample Similarity Matrix|sample similarity matrices]]. Univariate scores measure the alignment of a normalized feature with smooth nontrivial Laplacian directions, while multivariate extensions reconstruct the target similarity jointly and suppress redundant variables. This distinction separates spectral feature selection as a broad principle from any single ranking formula.

# References

[[dataclustering.pdf]]

[[spectralfeatureselectionfordatamining.pdf]]
