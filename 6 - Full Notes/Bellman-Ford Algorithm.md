2026-11-06 13:25

Status: #baby

Tags: [[Graph Algorithms]]

# Bellman-Ford Algorithm

The Bellman-Ford algorithm finds single-source shortest paths even when a graph contains negative edge weights. Instead of finalizing the currently cheapest vertex as [[Dijkstra's Algorithm]] does, it repeatedly applies [[Graph Relaxation]] across every edge so improved distances can propagate through the graph.

After at most $V-1$ passes, every finite shortest simple path has had enough opportunities to propagate through its edges. An additional pass tests for a reachable [[Negative Cycle]]: if any distance can still be reduced, repeated traversal can lower the cost without bound and no finite shortest path exists for affected vertices.

The broader lesson is that input constraints select the algorithm. Nonnegative latency or distance permits Dijkstra's more selective processing, while gains, credits, or other negative-valued transitions invalidate that assumption and require a method that revisits estimates.

# References

[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
