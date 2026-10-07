2026-10-07 00:46

Status: #baby

Tags: [[Multi-Source Feature Selection]]

# Probabilistic Rank Aggregation

Probabilistic rank aggregation treats each input ranking as a component that may explain a feature's relevance. A rank-to-probability function gives more weight to high positions, while a mixture coefficient represents the reliability of each ranking source.

An expectation-maximization procedure estimates the mixture coefficients from a chosen feature set. Using known relevant features yields supervised aggregation; using the full feature collection yields an unsupervised form. Final scores marginalize across ranking sources, so strong evidence from reliable lists outweighs agreement from weak lists.

# References

[[spectralfeatureselectionfordatamining.pdf]]

