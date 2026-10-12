2026-09-30 21:11

Status: #baby

Tags: [[Reinforcement Learning Methods]]

# Q-Learning

Q-learning estimates the expected cumulative reward of taking an action in a state and then continuing with valuable choices. The Q value is an internal guide to future payoff, not necessarily a reward received immediately from the environment.

Each transition supplies a [[Temporal Difference Learning|temporal-difference]] update that combines observed reward with a discounted estimate of what can be obtained from the next state. Once the estimates are useful, a learner can select actions with high Q values while retaining enough exploration to correct incomplete beliefs.

# References

[[machinelearning_mit.epub]]
