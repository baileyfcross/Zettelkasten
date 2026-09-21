2026-09-20 23:34

Status: #baby

Tags: [[Game Artificial Intelligence]]

# Static Evaluation Function

A static evaluation function estimates the desirability of a nonterminal game state when adversarial search cannot expand the complete [[Game Tree]]. It combines measurable features into a score from the current player's perspective.

The function must be quick because search invokes it at many leaves. Its approximation shapes the decisions of depth-limited [[Minimax]], so feature weights and blind spots can matter more than searching one additional shallow branch.

# References

[[gameprogrammingincplusplus.pdf]]
