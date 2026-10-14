2026-09-17 09:48

Status: #baby

Tags: [[Big Data Preprocessing]]

# Feature Subset Selection

Feature subset selection returns a chosen set of original variables judged useful for the analytical task. It differs from [[Feature Ranking]], which orders variables but does not by itself define the final subset.

Searching all possible subsets becomes exponential as dimensionality grows. Practical methods therefore use heuristics, model structure, or distributed computation while accepting that the globally best combination may remain unknown.

Multivariate spectral methods formulate the subset indirectly through row sparsity or greedily reconstruct a target similarity matrix. These approaches evaluate variables in the context of those already selected, allowing the subset objective to account for redundancy that a simple [[Feature Ranking]] cannot detect.

# References

[[frontiersofdatascience.pdf]]

[[spectralfeatureselectionfordatamining.pdf]]
