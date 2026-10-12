2026-09-29 19:17

Status: #baby

Tags: [[High-Dimensional Graphical Models]]

# Neighborhood Selection for Gaussian Graphs

Neighborhood selection estimates a Gaussian graph by regressing each variable on all the others with a sparse penalty. A nonzero regression coefficient indicates a candidate neighbor because Gaussian conditional means are determined by the precision matrix.

Separate Lasso regressions are easy to compute but may disagree about whether $a$ is adjacent to $b$. An OR or AND rule can symmetrize the result, while a paired group penalty enforces symmetric zeros directly at greater computational cost. Sparse degree, rather than merely a sparse total edge count, governs high-dimensional feasibility.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
