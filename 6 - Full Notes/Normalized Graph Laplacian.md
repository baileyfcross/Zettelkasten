2026-10-07 00:46

Status: #baby

Tags: [[Spectral Feature Scoring and Graph Structure]]

# Normalized Graph Laplacian

For an undirected weighted graph with adjacency matrix $A$, degree matrix $D$, and [[Graph Laplacian]] $L=D-A$, the normalized graph Laplacian is $\mathcal{L}=D^{-1/2}LD^{-1/2}$.

Normalization adjusts each vertex contribution by local degree, so a dense neighborhood does not dominate merely because it has more incident weight. The matrix is positive semidefinite, its eigenvalues lie between zero and two, and its trivial zero-eigenvalue direction is proportional to $D^{1/2}\mathbf{1}$. Its leading nontrivial eigenvectors encode smooth, large-scale graph structure used by [[Spectral Feature Selection]].

# References

[[spectralfeatureselectionfordatamining.pdf]]

