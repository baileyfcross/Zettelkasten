2026-09-06 00:13

Status: #baby

Tags: [[Graph Algorithms]]

# Negative Cycle

A negative cycle is a [[Graph Cycle]] whose edge weights sum to a negative value. Repeating the cycle reduces a route's accumulated cost every time it is traversed.

If such a cycle is reachable in a shortest-path problem, no finite shortest path exists for affected destinations because the path length can always be made smaller. This is more than a limitation of [[Dijkstra's Algorithm]]; the requested optimum itself is undefined.

The [[Bellman-Ford Algorithm]] detects this condition by performing one additional relaxation pass after the passes needed to propagate every finite simple path. If an estimate can still improve, some reachable negative cycle is continuing to lower it.

# References

[[algorithms.epub]]
[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
