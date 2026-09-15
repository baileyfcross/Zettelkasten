2026-09-14 21:34

Status: #baby

Tags: [[Matrix Factorization and Spectral Clustering]]

# NMF Multiplicative Update

A multiplicative update alternately rescales the two nonnegative factors using ratios of terms derived from the reconstruction objective. Starting from nonnegative values, the updates preserve nonnegativity without a separate projection step.

The objective is nonconvex in both factors together, so the procedure can reach different stationary solutions from different initializations. Small entries may also change slowly, making stopping rules and numerical safeguards important.

# References

[[dataclustering.pdf]]

