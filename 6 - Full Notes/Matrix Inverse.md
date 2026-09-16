2026-09-06 19:44

Status: #baby

Tags: [[Matrix and Vector Computation]] · [[Matrix Algebra for Statistical Models]] · [[FEM Mathematical Foundations]]

# Matrix Inverse

An inverse of a square matrix $A$ is a matrix $A^{-1}$ satisfying $AA^{-1}=A^{-1}A=I$. It exists only when $A$ is a [[Nonsingular Matrix]], equivalently when its [[Determinant]] is nonzero.

For a system $Ax=b$, multiplication by the inverse gives $x=A^{-1}b$. In computation, a direct solver or [[LU Decomposition]] is usually preferable to explicitly forming the inverse.

The closed-form least-squares expression includes the inverse of the design cross-product, but the source cautions that explicitly computing it with `solve` can be numerically unstable. A [[QR Decomposition]] is preferred for fitting in practical software.

The primer expresses formal finite element solutions through an inverse of the reduced global matrix. For large assembled systems, solving the equations directly is preferable to explicitly constructing that inverse.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]

[[finiteelementanalysis_aprimer.pdf]]
