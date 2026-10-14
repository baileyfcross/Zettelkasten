2026-09-29 19:17

Status: #baby

Tags: [[High-Dimensional Graphical Models]]

# Graph Moralization

Graph moralization converts a [[Directed Acyclic Graph]] into an [[Undirected Graph]] by connecting every pair of parents that share a child and then replacing all arrows with undirected edges. The added parent-to-parent edges preserve dependencies created by conditioning on their common child.

If a positive-density distribution is Markov with respect to the original directed graph, it is also Markov with respect to the moral graph. The moral graph need not be the minimal undirected representation, so moralization is a valid conversion rather than a guarantee of the sparsest dependency graph.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
