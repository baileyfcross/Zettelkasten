2026-09-06 00:13

Status: #baby

Tags: [[Matrix and Vector Computation]] · [[Graph Structures]]

# Adjacency Matrix

An adjacency matrix represents a [[Graph]] with one row and one column for every [[Vertex]]. An entry is one when the corresponding pair is connected by an edge and zero when that connection is absent.

For a [[Directed Graph]], the row and column order preserves edge direction. This matrix supplies the link structure from which PageRank constructs a normalized [[Hyperlink Matrix]].

Matrix powers encode longer connectivity: the $(i,j)$ entry of $A^k$ counts length-$k$ walks from vertex $i$ to vertex $j$ under the chosen row-column convention. Degree information from $A$ also feeds the [[Graph Laplacian]].

# References

[[algorithms.epub]]

[[linearalgebra.pdf]]
