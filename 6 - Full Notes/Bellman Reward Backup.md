2026-09-30 21:11

Status: #baby

Tags: [[Reinforcement Learning Methods]]

# Bellman Reward Backup

A Bellman reward backup relates the value of a state-action choice to its immediate reward and the discounted value available after the transition. It lets information about a later outcome move backward to choices that made that outcome reachable.

Discounting gives a reward less influence when it lies farther in the future or is reached through uncertain transitions. Repeated backups over experienced paths allow early actions with no immediate payoff to acquire value because of their connection to a later real reward; [[Temporal Difference Learning]] performs this update incrementally.

# References

[[machinelearning_mit.epub]]
