2026-10-07 00:46

Status: #baby

Tags: [[Multivariate Spectral Feature Selection]]

# Residual Similarity Matrix Update

A residual similarity matrix records the part of a target pairwise structure not yet reconstructed by selected features. Starting from $R=S$, selecting a normalized feature $f$ updates the residual as $R\leftarrow R-ff^T$.

The next feature is scored against the updated residual rather than the original target. This makes a greedy [[Matrix Comparison Spectral Feature Selection]] sensitive to redundancy: a candidate aligned mainly with structure already removed receives a smaller marginal score.

# References

[[spectralfeatureselectionfordatamining.pdf]]

