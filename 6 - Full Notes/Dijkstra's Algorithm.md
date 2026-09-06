2026-09-06 00:13

Status: #baby

Tags: [[Graph Algorithms]]

# Dijkstra's Algorithm

Dijkstra's algorithm finds the shortest paths from one starting vertex to all other vertices in a graph with nonnegative edge weights. It initializes the start at distance zero and every other vertex at infinity.

The algorithm repeatedly selects the unvisited vertex with the smallest current estimate and applies [[Graph Relaxation]] to its neighbors. Recording each improved vertex's predecessor makes it possible to reconstruct a route after the final distances are known. Negative weights violate the assumptions that make a visited estimate final.

# References

[[algorithms.epub]]
