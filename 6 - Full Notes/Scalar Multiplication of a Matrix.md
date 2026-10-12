2026-09-06 19:44

Status: #baby

Tags: [[Matrix and Vector Computation]] · [[FEM Mathematical Foundations]]

# Scalar Multiplication of a Matrix

Scalar multiplication multiplies every entry of a [[Matrix]] by the same number. For $A=(a_{ij})$ and scalar $k$, the matrix $kA$ has entries $ka_{ij}$ and keeps the dimensions of $A$.

It distributes over [[Matrix Addition]] and over addition of scalars. Multiplication by zero produces the [[Zero Matrix]], while multiplication by $-1$ produces the additive inverse of the matrix.

Finite element characteristic matrices often appear as a geometric matrix multiplied by a scalar material-and-size factor, such as axial rigidity divided by element length. Scalar multiplication preserves the matrix pattern while changing its physical scale.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[finiteelementanalysis_aprimer.pdf]]
