2026-09-06 00:13

Status: #baby

Tags: [[Graph Algorithms]]

# Hierholzer's Algorithm

Hierholzer's algorithm finds an [[Eulerian Circuit]] in a graph that contains one. Starting at a vertex, it follows unused edges until it returns to that vertex and forms an initial closed tour.

If a vertex on the current tour still touches an unused edge, the algorithm starts another unused-edge tour there and splices the new circuit into the old one. Repeating this process incorporates every edge. With an appropriate implementation, the work is linear in the number of edges.

# References

[[algorithms.epub]]
