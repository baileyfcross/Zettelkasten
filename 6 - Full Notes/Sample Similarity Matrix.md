2026-10-07 00:46

Status: #baby

Tags: [[Spectral Feature Scoring and Graph Structure]]

# Sample Similarity Matrix

A sample similarity matrix stores the pairwise affinities among observations. Its entry $s_{ij}$ records how strongly sample $i$ resembles sample $j$, allowing class membership, neighborhood geometry, or another target concept to be expressed in one common representation.

Unsupervised construction can use a radial-basis, polynomial, linear, or cosine kernel, while supervised construction can assign positive similarity only to members of the same class. The matrix can then define a weighted [[Graph]] whose spectrum guides [[Spectral Feature Selection]]. Its usefulness depends on whether the chosen similarity actually represents the relationships the analysis should preserve.

# References

[[spectralfeatureselectionfordatamining.pdf]]

