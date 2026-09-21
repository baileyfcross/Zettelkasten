2026-09-20 23:34

Status: #baby

Tags: [[Game Artificial Intelligence]]

# Greedy Best-First Search

Greedy best-first search expands the frontier node with the smallest heuristic estimate to the goal. It follows apparently promising directions without including the path cost already accumulated.

The focus can reduce exploration, but the returned path is not guaranteed to be shortest and a misleading heuristic can send the search into poor regions. [[A Star Search]] balances the same estimate with cost from the start.

# References

[[gameprogrammingincplusplus.pdf]]
