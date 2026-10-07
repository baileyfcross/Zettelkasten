2026-10-07 00:46

Status: #baby

Tags: [[Parallel Spectral Feature Selection]]

# Parallel MRSF

Parallel MRSF distributes the costly sample-wise operations of [[Minimal Redundancy Spectral Feature Selection]] while keeping the small active-set state on a coordinator. Workers calculate feature-target correlations, active-feature Gram matrices, residual correlations, and local residual updates.

The coordinator chooses entrants, updates the regularization path, and solves or validates the reduced active-set problem from aggregated statistics. Near-linear speedup is possible when the sample count per worker is large and the active set and output dimension remain small relative to the full data.

# References

[[spectralfeatureselectionfordatamining.pdf]]

