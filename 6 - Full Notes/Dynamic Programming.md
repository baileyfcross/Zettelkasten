2026-11-06 13:25

Status: #baby

Tags: [[Algorithm Foundations]]

# Dynamic Programming

Dynamic programming solves a problem by reusing answers to smaller subproblems instead of recomputing the same states. It is useful when the problem has overlapping subproblems and an optimal substructure, meaning a larger optimum can be assembled from optimal answers to smaller cases.

A dynamic-programming design identifies four elements: a state containing the minimum information needed to describe one subproblem, a transition that relates a state to simpler states, base cases that anchor the calculation, and an order in which states are evaluated. Choosing the state is usually the decisive design step because an incomplete state cannot produce a correct transition while an oversized state wastes time and memory.

[[Memoization and Tabulation]] are the two common evaluation styles. Both exchange storage for reduced computation, and both can turn repeated exponential work into a controlled set of states, although some problems such as [[Zero-One Knapsack Problem]] remain pseudo-polynomial in a numeric capacity.

# References

[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
