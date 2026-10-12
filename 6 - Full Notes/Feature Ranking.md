2026-09-17 09:48

Status: #baby

Tags: [[Big Data Preprocessing]]

# Feature Ranking

Feature ranking orders variables according to a relevance score or other selection criterion. Some rankers also report a weight that indicates the strength assigned by the internal metric.

A ranking is not automatically a subset because a cutoff still must be chosen and individually strong variables may be redundant together. It is useful when users need a transparent order or when exhaustive subset search is infeasible.

In spectral ranking, a feature's score measures alignment with a target similarity operator or selected Laplacian eigenvectors. The ranking can be generated efficiently by scoring each variable independently, but this same independence explains why the top positions may contain highly redundant variables.

# References

[[frontiersofdatascience.pdf]]

[[spectralfeatureselectionfordatamining.pdf]]
