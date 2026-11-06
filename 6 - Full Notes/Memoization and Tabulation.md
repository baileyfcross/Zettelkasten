2026-11-06 13:25

Status: #baby

Tags: [[Algorithm Complexity Analysis]]

# Memoization and Tabulation

Memoization and tabulation are two ways to evaluate a [[Dynamic Programming]] recurrence without repeatedly solving the same subproblem. Memoization preserves a top-down recursive structure and stores results when states are first encountered, so only states reachable from the original problem need to be evaluated.

Tabulation starts from base cases and fills a table toward larger states in a predetermined order. It avoids deep recursive calls, exposes memory use explicitly, and is often attractive in high-load Java code when the full state space and dependency order are known.

Neither style is universally superior. Memoization can match the conceptual recursion and skip unreachable states, while tabulation provides tighter control over stack depth, iteration order, and storage. The choice follows from the recurrence, reachable state space, and resource constraints.

# References

[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
