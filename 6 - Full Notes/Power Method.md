2026-09-06 00:13

Status: #baby

Tags: [[Matrix and Vector Computation]]

# Power Method

The power method starts with a [[Vector]] and repeatedly multiplies it by the same [[Matrix]]. Under the required conditions, the successive vectors converge toward the matrix's leading [[Eigenvector]].

PageRank begins with relative-importance values summing to one and repeatedly applies the Google matrix. When another iteration no longer changes the [[PageRank Vector]], the stable values provide the final ranking.

For a general matrix, each multiplication is normally followed by normalization to prevent overflow and expose the scale factor. Convergence requires a [[Dominant Eigenvalue]] and a starting vector with a nonzero component in its eigendirection; the [[Rayleigh Quotient]] can estimate the corresponding eigenvalue.

The asymptotic rate depends on the magnitude ratio between the second-largest and dominant eigenvalues. A ratio near one causes slow convergence, and sign changes in the dominant eigenvalue can make normalized iterates alternate even while their direction converges.

# References

[[algorithms.epub]]

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[statisticalcomputingincplusplusandr.pdf]]
