2026-09-06 00:13

Status: #baby

Tags: [[Graph Algorithms]]

# Greedy Algorithm

A greedy algorithm chooses the option with the greatest immediate benefit at each decision point. It follows an [[Algorithmic Heuristic]] that asks what looks best now instead of exhaustively planning every later consequence.

Greedy choices can be efficient and sometimes optimal, but they do not guarantee the [[Global Optimum]] in every problem. Edge coloring may use more colors than necessary, and choosing the smallest outgoing edge at each step need not produce the shortest complete route.

Correct use therefore requires an argument that the local choice cannot make an optimal solution worse and that the remaining subproblem retains the same structure. Earliest-finish interval scheduling has this exchange property, while choosing the best value-to-weight ratio does not solve the zero-one knapsack problem optimally.

# References

[[algorithms.epub]]
[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
