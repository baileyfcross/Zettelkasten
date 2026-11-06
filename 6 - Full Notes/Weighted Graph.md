2026-09-06 00:13

Status: #baby

Tags: [[Graph Structures]]

# Weighted Graph

A weighted graph attaches a numerical value to each [[Edge]]. The value expresses a property of the represented relationship, such as distance, duration, cost, reward, or penalty.

Weights change how a route is evaluated: the [[Graph Path Length]] becomes the sum of edge weights rather than simply the number of edges. [[Dijkstra's Algorithm]] finds shortest paths when the relevant weights are nonnegative.

The weight can model distance, latency, delivery cost, execution time, profit, or another transition consequence. This distinguishes minimum cost from minimum edge count: a path with more transitions can still be cheaper, so [[Breadth-First Search]] is sufficient only when all relevant edges have equal cost.

# References

[[algorithms.epub]]
[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
