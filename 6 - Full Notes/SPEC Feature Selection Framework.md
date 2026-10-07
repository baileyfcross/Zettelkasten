2026-10-07 00:46

Status: #baby

Tags: [[Spectral Feature Scoring and Graph Structure]]

# SPEC Feature Selection Framework

SPEC is a univariate [[Filter Feature Selection Model]] that ranks features by their consistency with the spectrum of a graph derived from a [[Sample Similarity Matrix]]. It constructs the graph and normalized Laplacian, normalizes each feature by graph degree, evaluates a spectral ranking function, and returns the requested number of top-ranked features.

Its three configurable parts are the similarity matrix, a [[Spectral Matrix Function]], and the feature-ranking rule. Changing how the similarity matrix uses labels produces supervised, unsupervised, or semi-supervised selection while retaining the same overall mechanism. Because features are scored independently, SPEC does not by itself remove redundant features.

# References

[[spectralfeatureselectionfordatamining.pdf]]

