2026-09-06 00:13

Status: #baby

Tags: [[Graph Structures]] · [[High-Dimensional Graphical Models]]

# Undirected Graph

An undirected graph has edges that can be traversed in either direction. An edge connecting vertices $A$ and $B$ therefore represents the same connection whether it is approached from $A$ or from $B$.

Reciprocal social relationships and two-way bridges can be modeled this way. When the direction of a relationship matters, the appropriate model is instead a [[Directed Graph]].

In an undirected graphical model, a node is conditionally independent of nonneighbors given its neighbors. For positive continuous densities there is a unique minimal graph with this property, and the density factorizes over graph cliques. This makes undirected graphs suitable for learning conditional-dependence structure when arrow direction is not identifiable.

# References

[[algorithms.epub]]

[[introductiontohigh-dimensionalstatistics.pdf]]
