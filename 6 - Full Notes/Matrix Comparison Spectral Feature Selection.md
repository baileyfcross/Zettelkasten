2026-10-07 00:46

Status: #baby

Tags: [[Multivariate Spectral Feature Selection]]

# Matrix Comparison Spectral Feature Selection

Matrix Comparison Spectral Feature Selection, or MCSF, greedily selects features whose outer products best reconstruct a target [[Sample Similarity Matrix]]. It compares the kernel induced by the selected original features with the desired similarity structure.

After each selection, the chosen feature's outer product is subtracted from the current residual matrix. Subsequent candidates are evaluated against what remains unexplained, which discourages repeatedly selecting correlated features. The method is simpler than the regression-based MRSF formulation but optimizes a greedy sequence rather than a joint convex objective.

# References

[[spectralfeatureselectionfordatamining.pdf]]

