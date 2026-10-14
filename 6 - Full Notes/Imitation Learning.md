2026-09-30 21:11

Status: #baby

Tags: [[Reinforcement Learning Methods]]

# Imitation Learning

Imitation learning uses demonstrations from someone who can already perform a task to reduce the amount of unguided exploration required from an agent. It is especially useful when random actions are slow, costly, or capable of harming the agent or its environment.

The demonstration can be used directly as state-action supervision through [[Behavioral Cloning]], or it can be analyzed to infer the objective through [[Inverse Reinforcement Learning]]. Demonstrations narrow the search, but they also carry the demonstrator's limitations and may not cover states reached after a learner makes a mistake.

# References

[[machinelearning_mit.epub]]
