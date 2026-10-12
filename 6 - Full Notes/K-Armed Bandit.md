2026-09-30 21:11

Status: #baby

Tags: [[Reinforcement Learning Methods]]

# K-Armed Bandit

A K-armed bandit is a simplified reinforcement-learning problem with one state and K available actions. Each action returns a reward drawn from its own unknown process, and the learner must choose actions so that its accumulated reward is large.

One trial is insufficient when rewards are random, so the value of an action is estimated from repeated observations. The problem isolates the [[Exploration-Exploitation Tradeoff]]: exploiting the action with the highest current estimate earns reward, while exploring less-known actions may reveal a better choice.

A recommender can treat candidate strategies or presentations as bandit arms and use clicks, watch time, or another defined outcome as reward. An epsilon-greedy policy usually sends traffic to the current best arm while reserving a small fraction for random exploration, allowing evidence to move progressively toward a winner rather than waiting for a fixed experiment to end.

# References

[[machinelearning_mit.epub]]

[[recommendationengines.epub]]
