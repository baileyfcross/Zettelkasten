2026-09-06 00:13

Status: #baby

Tags: [[Matrix and Vector Computation]] · [[Matrix Algebra for Statistical Models]] · [[FEM Mathematical Foundations]]

# Matrix Multiplication

Matrix multiplication combines two compatible matrices by taking each row from the first matrix with each column from the second. The corresponding values are multiplied and their products summed to form one entry in the result.

The operation expresses many related calculations at once. PageRank uses repeated [[Vector-Matrix Multiplication]], while neural networks can calculate the weighted inputs of many artificial neurons through large matrix operations.

If $A$ has size $m\times n$ and $B$ has size $n\times p$, then $AB$ has size $m\times p$ and entry $(i,j)$ is the dot product of row $i$ of $A$ with column $j$ of $B$. Matrix multiplication is associative and distributive but generally not commutative: even when both products exist, $AB$ need not equal $BA$.

In a linear model, multiplying the design matrix by the coefficient vector produces a fitted value for every experimental unit at once. R uses `%*%` for this operation, distinguishing it from element-wise multiplication.

Finite element equations use matrix products to map nodal unknowns into loads, strains, stresses, gradients, and fluxes. The order of multiplication matters because coefficient, interpolation, and field vectors have specific compatible dimensions.

# References

[[algorithms.epub]]

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]

[[finiteelementanalysis_aprimer.pdf]]
