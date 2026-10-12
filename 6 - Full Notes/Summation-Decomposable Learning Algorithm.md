2026-10-07 00:46

Status: #baby

Tags: [[Parallel Spectral Feature Selection]]

# Summation-Decomposable Learning Algorithm

A summation-decomposable learning algorithm expresses its expensive global statistics as sums of contributions from individual samples or sample partitions. Workers can calculate the local terms independently, and a reduction combines them into the statistic required by the model.

For example, linear regression uses $X^TX=\sum_i x_ix_i^T$ and $X^Ty=\sum_i y_ix_i$. The same structure supports distributed feature scoring and optimization. Scalability depends on local work dominating the cost of communicating and aggregating the partial results.

# References

[[spectralfeatureselectionfordatamining.pdf]]

