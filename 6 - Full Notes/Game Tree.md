2026-09-20 23:34

Status: #baby

Tags: [[Game Artificial Intelligence]]

# Game Tree

A game tree represents possible future states of an adversarial turn-based game. Each edge is a legal move, each level alternates the player to act, and terminal leaves record wins, losses, draws, or scores.

Complete trees grow too rapidly for most interesting games, so search stops at a depth limit and applies a [[Static Evaluation Function]]. [[Minimax]] then propagates estimated values back toward the current decision.

# References

[[gameprogrammingincplusplus.pdf]]
