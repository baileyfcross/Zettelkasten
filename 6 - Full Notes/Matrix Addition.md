2026-09-06 19:44

Status: #baby

Tags: [[Matrix and Vector Computation]] · [[FEM Mathematical Foundations]] · [[R Matrix Systems and Scientific Models]]

# Matrix Addition

Matrix addition combines two matrices of the same size by adding corresponding entries. If $A=(a_{ij})$ and $B=(b_{ij})$, then $A+B=(a_{ij}+b_{ij})$. The result has the same dimensions as both inputs.

The operation is commutative and associative, and the [[Zero Matrix]] acts as its additive identity. Matrix subtraction is addition of a [[Scalar Multiplication of a Matrix|scalar multiple]] by $-1$.

During finite element assembly, matrices from elements sharing a degree of freedom contribute by addition to the corresponding global entries. Compatible dimensions and consistent local-to-global numbering are therefore essential.

The student companion demonstrates addition and subtraction directly on R matrices and emphasizes the shared-dimension requirement. The concise syntax does not relax the mathematical rule: differently shaped arrays do not represent corresponding entries that can be combined.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[finiteelementanalysis_aprimer.pdf]]

[[rstudentcompanion.pdf]]
