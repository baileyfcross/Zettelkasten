2026-09-30 21:11

Status: #baby

Tags: [[Reinforcement Learning Methods]]

# Temporal Difference Learning

Temporal difference learning updates an estimate by comparing it with a target formed from a later estimate and any newly observed reward. It learns before an entire episode is complete by backing information from consecutive state-action choices through a [[Bellman Reward Backup]].

An action just before a goal can inherit a discounted portion of the goal's reward, and the preceding action can inherit a further-discounted value. Averaging these updates over many trials accounts for different paths and uncertain outcomes. [[Q-Learning]] applies this logic to values associated with state-action pairs.

# References

[[machinelearning_mit.epub]]
