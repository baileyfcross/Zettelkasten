2026-09-20 23:34

Status: #baby

Tags: [[Game Artificial Intelligence]]

# Alpha-Beta Pruning

Alpha-beta pruning accelerates [[Minimax]] by abandoning branches that cannot change the final decision. Alpha tracks the best value already guaranteed to the maximizing player, and beta tracks the best value guaranteed to the minimizing player.

When a branch proves no better than an established alternative, its remaining descendants need not be evaluated. The result is identical to ordinary minimax, but good move ordering can reduce the number of searched nodes dramatically.

# References

[[gameprogrammingincplusplus.pdf]]
