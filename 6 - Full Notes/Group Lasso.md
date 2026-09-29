2026-09-29 19:17

Status: #baby

Tags: [[Sparse and Structured Regression]]

# Group Lasso

Group Lasso partitions coefficients into predefined groups and penalizes the sum of their Euclidean norms. Its nonsmooth group norms make entire coefficient blocks become zero together, so selection occurs at the group level.

Weights can adjust for group size so large groups are not penalized merely for having more coordinates. When the true structure is group-sparse, its risk bound can avoid paying a separate $\log p$ cost for every active coordinate. The method assumes the grouping is meaningful; [[Sparse-Group Lasso]] adds within-group selection when active groups may themselves be sparse.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
