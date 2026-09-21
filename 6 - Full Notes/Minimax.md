2026-09-20 23:34

Status: #baby

Tags: [[Game Artificial Intelligence]]

# Minimax

Minimax selects a move under the assumption that the current player maximizes the evaluated outcome while the opponent minimizes it. Values are propagated upward through alternating maximum and minimum layers of a [[Game Tree]].

The algorithm is exact only when it reaches terminal states and their values are accurate. Depth-limited search substitutes a [[Static Evaluation Function]], and [[Alpha-Beta Pruning]] avoids branches that cannot affect the final choice.

# References

[[gameprogrammingincplusplus.pdf]]
