2026-10-07 00:46

Status: #baby

Tags: [[Multivariate Spectral Feature Selection]]

# Minimal Redundancy Spectral Feature Selection

Minimal Redundancy Spectral Feature Selection, or MRSF, solves a row-sparse multi-output regression problem whose targets encode a desired sample-similarity structure. It selects features jointly, so a candidate that duplicates information already represented by the active set receives less value than an equally relevant but complementary candidate.

MRSF follows a solution path until the requested number of features is active. At each stage it proposes a new active feature, solves a smaller regularized problem on the active set, and checks global optimality against every inactive feature. This avoids repeatedly solving the full problem for many arbitrary penalty values.

# References

[[spectralfeatureselectionfordatamining.pdf]]

