2026-09-06 00:13

Status: #baby

Tags: [[Graph Algorithms]]

# Negative Cycle

A negative cycle is a [[Graph Cycle]] whose edge weights sum to a negative value. Repeating the cycle reduces a route's accumulated cost every time it is traversed.

If such a cycle is reachable in a shortest-path problem, no finite shortest path exists for affected destinations because the path length can always be made smaller. This is more than a limitation of [[Dijkstra's Algorithm]]; the requested optimum itself is undefined.

# References

[[algorithms.epub]]
