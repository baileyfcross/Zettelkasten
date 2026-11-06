2026-09-20 23:34

Status: #baby

Tags: [[Game Artificial Intelligence]] · [[Graph Algorithms]]

# Breadth-First Search

Breadth-first search explores a graph in layers of increasing edge count from the start node. A queue holds discovered nodes, and each node records whether it has been visited and which predecessor first reached it.

On an unweighted graph, the first discovered path to a node uses the fewest edges, so the algorithm guarantees a shortest path when one exists. Weighted travel costs require a method such as [[Dijkstra's Algorithm]] or [[A Star Search]].

Recording the number of queued nodes at the start of an iteration lets a tree traversal process exactly one level before moving to the next. The queue is therefore not incidental storage: its first-in, first-out discipline creates the layer-by-layer behavior used for nearest vertices, minimum transition counts, and level-order output.

# References

[[gameprogrammingincplusplus.pdf]]
[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
