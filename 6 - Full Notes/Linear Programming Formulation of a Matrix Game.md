2026-10-03 22:06

Status: #baby

Tags: [[Matrix Game Theory]]

# Linear Programming Formulation of a Matrix Game

A rectangular zero-sum game without a saddle point can be converted into a linear program. The row player's probabilities are constrained so every opposing pure strategy yields at least a guaranteed value, while the column player's probabilities bound every row payoff above by its guaranteed loss.

Scaling the probabilities by the positive game value removes the ratio and produces dual linear programs. Solving them by the [[Simplex Method]] yields both players' optimal mixed strategies and the reciprocal scaling recovers the game's value.

# References

[[optimizationusinglinearprogramming.pdf]]

