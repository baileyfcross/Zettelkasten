2026-09-20 23:34

Status: #baby

Tags: [[Game Artificial Intelligence]]

# Breadth-First Search

Breadth-first search explores a graph in layers of increasing edge count from the start node. A queue holds discovered nodes, and each node records whether it has been visited and which predecessor first reached it.

On an unweighted graph, the first discovered path to a node uses the fewest edges, so the algorithm guarantees a shortest path when one exists. Weighted travel costs require a method such as [[Dijkstra's Algorithm]] or [[A Star Search]].

# References

[[gameprogrammingincplusplus.pdf]]
