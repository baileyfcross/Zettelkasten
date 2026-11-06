2026-11-06 13:25

Status: #baby

Tags: [[Graph Structures]]

# Adjacency List

An adjacency list represents a [[Graph]] by storing, for each [[Vertex]], the collection of edges leaving that vertex. A weighted form stores the destination and edge weight together, while the source is implied by the list in which the edge appears.

The representation uses space proportional to $V+E$ and lets traversal inspect only the neighbors that actually exist. It is therefore well suited to sparse graphs such as service dependencies, workflows, social connections, and road networks in which each vertex connects to only a small part of the graph.

An [[Adjacency Matrix]] offers constant-time access to any possible vertex pair but allocates space for every pair. Choosing between the two representations depends on graph density and the operations the algorithm performs.

# References

[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
