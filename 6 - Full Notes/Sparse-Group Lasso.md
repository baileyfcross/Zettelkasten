2026-09-29 19:17

Status: #baby

Tags: [[Sparse and Structured Regression]]

# Sparse-Group Lasso

Sparse-group Lasso combines a sum of group norms with an ordinary $\ell_1$ penalty. The group term can remove entire predefined blocks, while the coordinate term can set individual coefficients to zero inside the blocks that remain.

This matches a two-level structure in which only a few groups matter and each active group contains only a few relevant variables. The two penalty strengths determine the balance between group selection and within-group sparsity. Unlike [[Group Lasso]], it need not keep every coordinate in a selected group.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
