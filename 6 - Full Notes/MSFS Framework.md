2026-10-07 00:46

Status: #baby

Tags: [[Multi-Source Feature Selection]]

# MSFS Framework

The MSFS framework performs multi-source feature selection in three stages. It converts each external source into a local [[Sample Similarity Matrix]], applies [[Similarity Matrix Fusion]] to obtain a global similarity pattern, and supplies that pattern to a spectral selector.

Using sample similarity as the common representation allows heterogeneous sources about samples or features to enter one pipeline. The restriction is also its limitation: every useful source must be translated into pairwise sample relationships even when a feature graph or ranking would be a more natural representation.

# References

[[spectralfeatureselectionfordatamining.pdf]]

