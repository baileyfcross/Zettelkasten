2026-11-06 13:25

Status: #baby

Tags: [[Graph Algorithms]]

# Depth-First Search

Depth-first search explores one branch of a tree or graph as far as possible before backtracking. Recursion uses the call stack to remember unfinished vertices, while an iterative implementation stores the same frontier explicitly in a [[Stack]].

A visited set prevents repeated work and infinite traversal, but detecting a directed [[Graph Cycle]] requires distinguishing fully processed vertices from those still on the active path. Re-entering an active-path vertex closes a loop; merely reaching a fully processed vertex by another path does not prove a cycle.

For an adjacency-list graph, traversal takes $O(V+E)$ time because every reachable vertex and edge is processed at most a constant number of times. The pattern supports connected-component discovery, dependency analysis, topological reasoning, and recursive tree computations that combine child results.

# References

[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
