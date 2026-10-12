2026-09-30 00:59

Status: #baby

Tags: [[Graph Structures]]

# Graph Laplacian

For a finite graph with adjacency matrix $A$ and diagonal degree matrix $D$, the graph Laplacian is $L=D-A$. For an undirected graph it is symmetric and positive semidefinite.

The multiplicity of eigenvalue zero equals the number of connected components. The second-smallest eigenvalue is the graph's [[Algebraic Connectivity]], linking spectral information to how strongly the graph is joined.

Its quadratic form satisfies $x^TLx=\frac12\sum_{i,j}a_{ij}(x_i-x_j)^2$, so it measures how abruptly a signal changes across weighted edges. Degree normalization yields the [[Normalized Graph Laplacian]], whose leading nontrivial eigenvectors provide smooth directions for clustering and feature evaluation.

# References

[[linearalgebra.pdf]]

[[spectralfeatureselectionfordatamining.pdf]]
