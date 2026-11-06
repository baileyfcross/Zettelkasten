2026-09-18 17:13

Status: #baby

Tags: [[Game Artificial Intelligence]] · [[Graph Algorithms]]

# A Star Search

A-star search finds a low-cost path through a graph by prioritizing the sum of cost already incurred and a heuristic estimate of remaining cost. The first term preserves evidence from the explored route; the second directs exploration toward the goal.

With an [[Admissible Heuristic]], A-star can return an optimal path. Games apply it to grids, path-node networks, and navigation meshes.

Its priority is commonly expressed as $f(n)=g(n)+h(n)$, combining the cost already traveled with an estimate of the remaining cost. Setting the heuristic to zero recovers Dijkstra-like behavior; a well-informed admissible heuristic reduces the explored region, while graph-search implementations commonly also require consistency so estimates behave monotonically along edges.

# References

[[gameprogrammingincplusplus.pdf]]
[[gameprogrammingalgorithmsandtechniques.pdf]]
[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
