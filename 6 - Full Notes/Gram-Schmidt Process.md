2026-09-30 00:59

Status: #baby

Tags: [[Orthogonal Bases and Projections]]

# Gram-Schmidt Process

The Gram-Schmidt process converts a linearly independent sequence into an [[Orthogonal Basis]] for the same span. Each new vector is formed by subtracting from the next input vector its projections onto all previously constructed orthogonal directions.

Normalizing the results produces an [[Orthonormal Basis]]. Applied to the columns of a full-rank matrix, the process also yields a [[QR Decomposition]].

Classical Gram-Schmidt forms all projections from the original input vector, which can lose orthogonality in finite precision. Modified Gram-Schmidt subtracts one projection at a time from the evolving residual and is generally more numerically stable while producing the same exact-arithmetic factorization.

# References

[[linearalgebra.pdf]]

[[statisticalcomputingincplusplusandr.pdf]]
