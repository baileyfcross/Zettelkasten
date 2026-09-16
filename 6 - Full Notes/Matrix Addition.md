2026-09-06 19:44

Status: #baby

Tags: [[Matrix and Vector Computation]] · [[FEM Mathematical Foundations]]

# Matrix Addition

Matrix addition combines two matrices of the same size by adding corresponding entries. If $A=(a_{ij})$ and $B=(b_{ij})$, then $A+B=(a_{ij}+b_{ij})$. The result has the same dimensions as both inputs.

The operation is commutative and associative, and the [[Zero Matrix]] acts as its additive identity. Matrix subtraction is addition of a [[Scalar Multiplication of a Matrix|scalar multiple]] by $-1$.

During finite element assembly, matrices from elements sharing a degree of freedom contribute by addition to the corresponding global entries. Compatible dimensions and consistent local-to-global numbering are therefore essential.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[finiteelementanalysis_aprimer.pdf]]
