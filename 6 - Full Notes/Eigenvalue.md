2026-09-06 00:13

Status: #baby

Tags: [[Matrix and Vector Computation]]

# Eigenvalue

An eigenvalue is the scalar by which an [[Eigenvector]] is multiplied when a particular [[Matrix]] acts on it. The vector preserves its direction while its magnitude is scaled by this value.

The stable PageRank vector has eigenvalue one under the Google matrix because one more multiplication leaves it unchanged. The [[Power Method]] finds this leading eigenvector through repeated multiplication.

For a square matrix $A$, possible eigenvalues are the roots of the [[Characteristic Equation]] $\det(A-\lambda I)=0$. Their sum equals the [[Matrix Trace]] and their product is related to the [[Determinant]], counted with multiplicity.

More generally, an eigenvalue belongs to a linear operator whenever $T-\lambda I$ has a nontrivial kernel. Over an algebraically closed field the characteristic polynomial splits, but over other fields an operator need not have any eigenvalue in the field.

# References

[[algorithms.epub]]

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[linearalgebra.pdf]]
