2026-09-06 00:13

Status: #baby

Tags: [[Graph Structures]]

# Graph Cycle

A graph cycle is a [[Graph Path]] that returns to the vertex where it began. Its existence means that a traveler can follow a sequence of edges and come back to the starting point.

A graph without any cycle is acyclic. Direction matters in a [[Directed Graph]] because every edge in a directed cycle must be followed in its permitted direction. A [[Negative Cycle]] adds weights whose sum makes repeated traversal continually reduce path length.

In a directed depth-first traversal, encountering an already visited vertex is not enough to prove a cycle because two acyclic paths can converge. A cycle is detected when an edge returns to a vertex still on the active recursion path; fully processed vertices are tracked separately.

# References

[[algorithms.epub]]
[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
