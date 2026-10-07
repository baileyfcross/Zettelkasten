2026-10-07 00:46

Status: #baby

Tags: [[Spectral Feature Scoring and Graph Structure]]

# Normalized Cut Feature Score

A normalized cut feature score treats one feature as a soft partition of a sample graph and evaluates the corresponding degree-normalized cut. A low score means the feature changes little across high-similarity edges and separates the graph without favoring an arbitrarily tiny isolated group.

This interpretation connects [[Graph Signal Smoothness]] with [[Normalized Cut Relaxation]]. The normalization makes the score less sensitive to graph volume and some outliers, but the result remains conditional on the construction of the [[Sample Similarity Matrix]].

# References

[[spectralfeatureselectionfordatamining.pdf]]

