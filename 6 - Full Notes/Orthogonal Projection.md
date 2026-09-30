2026-09-14 20:21

Status: #baby

Tags: [[Distance Geometry and Dimension Reduction]] · [[Orthogonal Bases and Projections]]

# Orthogonal Projection

An orthogonal projection maps a point to the closest point in a specified linear subspace. The difference between the original and projected point is perpendicular to that subspace, which minimizes squared reconstruction distance.

Projecting samples onto selected basis directions produces lower-dimensional coordinates. In principal-component analysis, the chosen subspace maximizes retained variation and minimizes squared reconstruction error among linear subspaces of the same dimension.

When the subspace has an orthonormal basis $u_1,\ldots,u_k$, the projection is $\sum_i\langle v,u_i\rangle u_i$. This is the subspace component in the unique decomposition $v=p+q$ with $p$ in the subspace and $q$ in its orthogonal complement.

# References

[[dataanalysisforthelifescienceswithr.pdf]]

[[linearalgebra.pdf]]
