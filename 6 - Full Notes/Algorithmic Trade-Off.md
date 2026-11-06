2026-11-06 13:25

Status: #baby

Tags: [[Software Quality Attributes and Architecture Tradeoffs]]

# Algorithmic Trade-Off

An algorithmic trade-off exchanges one constrained resource or quality for another. A hash table or [[Trie]] spends memory to accelerate lookup, [[Dynamic Programming]] stores intermediate states to avoid repeated computation, and parallel execution adds coordination complexity in pursuit of shorter elapsed time.

Some trade-offs impose restrictions instead of consuming storage. [[Dijkstra's Algorithm]] gains efficiency by requiring nonnegative edge weights, while a greedy method gains simplicity by committing to local choices and therefore requires a proof that those choices preserve a global optimum.

The correct question is not which algorithm is universally fastest, but which cost the current task can afford. Input size, latency, memory, predictability, correctness guarantees, implementation complexity, operational burden, and future change all belong in that decision.

# References

[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
