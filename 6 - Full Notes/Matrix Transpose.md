2026-09-06 19:44

Status: #baby

Tags: [[Matrix and Vector Computation]] · [[Matrix Algebra for Statistical Models]] · [[FEM Mathematical Foundations]]

# Matrix Transpose

The transpose of a matrix exchanges its rows and columns. If $A$ is an $m\times n$ matrix, then $A^T$ is $n\times m$ and its entries satisfy $(A^T)_{ij}=a_{ji}$.

Transposition reverses the order of a product: $(AB)^T=B^TA^T$. A matrix equal to its transpose is a [[Symmetric Matrix]], while one equal to the negative of its transpose is a [[Skew-Symmetric Matrix]].

The source uses transposition to form dot products, sums of squares, and the normal equations. In R, `t` changes row orientation to column orientation so outcome and design matrices have compatible dimensions for these calculations.

Transposes enter variational finite element expressions when gradient or interpolation vectors form quadratic energy terms and symmetric element matrices. They also reverse the order of products during derivations.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]

[[finiteelementanalysis_aprimer.pdf]]
