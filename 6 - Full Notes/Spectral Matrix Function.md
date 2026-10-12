2026-10-07 00:46

Status: #baby

Tags: [[Spectral Feature Scoring and Graph Structure]]

# Spectral Matrix Function

For a symmetric matrix $L=U\Lambda U^T$, a spectral matrix function applies a scalar function to its eigenvalues: $\gamma(L)=U\gamma(\Lambda)U^T$. The eigenvectors remain fixed while each spectral direction is reweighted.

In [[SPEC Feature Selection Framework]], an increasing function such as $\gamma(\lambda)=\lambda^3$ enlarges the contrast between small leading eigenvalues and larger tail eigenvalues. This can penalize noisy, rapidly varying directions more strongly. Polynomial choices can be evaluated directly as matrix polynomials without forming a complete [[Spectral Decomposition of a Symmetric Matrix]].

# References

[[spectralfeatureselectionfordatamining.pdf]]

