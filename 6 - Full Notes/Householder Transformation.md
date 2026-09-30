2026-09-06 19:44

Status: #baby

Tags: [[Numerical Eigenvalue Methods]] · [[Orthogonal Bases and Projections]]

# Householder Transformation

A Householder transformation is an orthogonal reflection of the form $H=I-2uu^T/(u^Tu)$. It maps a vector onto a chosen coordinate direction and can zero many entries at once.

Successive reflections reduce a symmetric matrix to tridiagonal form or a general matrix toward Hessenberg form, preparing it for a [[QR Algorithm]].

Because a Householder matrix is symmetric, orthogonal, and its own inverse, it performs this elimination without changing Euclidean lengths. The same reflection construction is a stable building block for [[QR Decomposition]].

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[linearalgebra.pdf]]
