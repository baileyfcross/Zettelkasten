2026-09-30 21:11

Status: #baby

Tags: [[Reinforcement Learning Methods]]

# K-Armed Bandit

A K-armed bandit is a simplified reinforcement-learning problem with one state and K available actions. Each action returns a reward drawn from its own unknown process, and the learner must choose actions so that its accumulated reward is large.

One trial is insufficient when rewards are random, so the value of an action is estimated from repeated observations. The problem isolates the [[Exploration-Exploitation Tradeoff]]: exploiting the action with the highest current estimate earns reward, while exploring less-known actions may reveal a better choice.

# References

[[machinelearning_mit.epub]]
