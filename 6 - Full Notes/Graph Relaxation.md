2026-09-06 00:13

Status: #baby

Tags: [[Graph Algorithms]]

# Graph Relaxation

Graph relaxation improves a provisional estimate when a newly examined route is better. A shortest-path algorithm may begin with deliberately extreme estimates—zero for the starting vertex and infinity elsewhere—and replace them with progressively smaller distances.

In [[Dijkstra's Algorithm]], examining an edge from the current vertex asks whether the known distance to that vertex plus the edge weight beats the neighbor's current estimate. If so, both the distance and predecessor are updated.

# References

[[algorithms.epub]]
