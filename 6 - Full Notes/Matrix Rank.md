2026-09-06 19:44

Status: #baby

Tags: [[Matrix and Vector Computation]] · [[Matrix Algebra for Statistical Models]]

# Matrix Rank

The rank of a matrix is the number of linearly independent rows, which equals the number of linearly independent columns. It can be read as the number of pivots in a [[Row Echelon Form]].

Rank determines how much independent information a matrix contains. A square matrix has an inverse exactly when it has full rank, while rank comparisons of a [[Coefficient Matrix]] and its [[Augmented Matrix]] help determine whether a [[Linear System]] is consistent.

In a design matrix, rank counts the independently estimable columns. If rank is smaller than the number of model terms, the least-squares coefficients are not unique and at least one intended scientific effect cannot be separated from the others.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]
