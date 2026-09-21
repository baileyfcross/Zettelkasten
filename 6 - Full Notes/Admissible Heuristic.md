2026-09-18 17:13

Status: #baby

Tags: [[Game Artificial Intelligence]]

# Admissible Heuristic

An admissible heuristic never overestimates the true remaining cost from a search node to the goal. It may be optimistic, but it cannot claim that the goal is farther away than the cheapest possible route.

This property allows [[A Star Search]] to preserve optimality. Manhattan distance suits movement restricted to orthogonal grid steps, while Euclidean distance reflects unrestricted straight-line distance.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
