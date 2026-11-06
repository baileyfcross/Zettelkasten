2026-11-06 13:25

Status: #baby

Tags: [[Algorithm Complexity Analysis]]

# Zero-One Knapsack Problem

The zero-one knapsack problem selects whole items with weights and values so their total weight does not exceed a capacity and their total value is maximized. Each item has only two states—taken or skipped—so partial selection is not allowed.

A bottom-up [[Dynamic Programming]] solution uses a state such as `dp[item][capacity]`. If the current item does not fit, the state inherits the result without it; if it fits, the transition compares skipping it with adding its value to the best result for the remaining capacity. The zero-item and zero-capacity cases form the table's base row and column.

The two-dimensional table costs $O(nW)$ time and space for $n$ items and numeric capacity $W$. If only the maximum value is needed, storage can be reduced to $O(W)$; reconstructing the chosen set requires retaining decisions or walking backward through a completed table. The time is pseudo-polynomial because $W$ is a numeric value rather than the length of its encoded representation.

# References

[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
