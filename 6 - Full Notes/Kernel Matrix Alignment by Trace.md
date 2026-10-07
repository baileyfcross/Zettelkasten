2026-10-07 00:46

Status: #baby

Tags: [[Multivariate Spectral Feature Selection]]

# Kernel Matrix Alignment by Trace

For two normalized similarity or kernel matrices $K$ and $S$, $\operatorname{Trace}(KS)$ measures their alignment. The quantity is large when pairs receiving strong similarity in one matrix tend to receive strong similarity in the other.

If selected features form a data matrix $X_F$, their linear kernel $X_FX_F^T$ can be compared with a target [[Sample Similarity Matrix]] through this trace objective. The criterion turns feature scoring into an explicit structure-preservation problem, although normalization is necessary to prevent matrix scale from masquerading as agreement.

# References

[[spectralfeatureselectionfordatamining.pdf]]

