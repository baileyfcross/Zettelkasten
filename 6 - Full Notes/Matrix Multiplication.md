2026-09-06 00:13

Status: #baby

Tags: [[Matrix and Vector Computation]]

# Matrix Multiplication

Matrix multiplication combines two compatible matrices by taking each row from the first matrix with each column from the second. The corresponding values are multiplied and their products summed to form one entry in the result.

The operation expresses many related calculations at once. PageRank uses repeated [[Vector-Matrix Multiplication]], while neural networks can calculate the weighted inputs of many artificial neurons through large matrix operations.

If $A$ has size $m\times n$ and $B$ has size $n\times p$, then $AB$ has size $m\times p$ and entry $(i,j)$ is the dot product of row $i$ of $A$ with column $j$ of $B$. Matrix multiplication is associative and distributive but generally not commutative: even when both products exist, $AB$ need not equal $BA$.

# References

[[algorithms.epub]]

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]
