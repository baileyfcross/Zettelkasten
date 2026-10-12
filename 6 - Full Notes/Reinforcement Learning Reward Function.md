2026-09-30 21:11

Status: #baby

Tags: [[Reinforcement Learning Methods]] [[Artificial General Intelligence Architectures]]

# Reinforcement Learning Reward Function

A reinforcement-learning reward function defines the feedback that makes one outcome preferable to another. It states the task's objective without supplying the correct action for every state, which is why reinforcement learning is described as learning from a critic rather than from a teacher.

Rewards can be sparse and delayed, arriving only after a long action sequence. Intermediate value estimates are useful because they indicate progress toward the real reward, but they are not a replacement objective. A poorly chosen reward can teach behavior that maximizes the signal without accomplishing the intended task.

In a general agent, the reward function does more than score a bounded exercise: it determines which predicted future the system tries to bring about. Increasing capability therefore magnifies specification errors. The agent may satisfy the formal signal through a strategy that violates the designer's unstated intention, which connects reward design to [[Moral Reward Specification]] and the [[AI Control Problem]].

# References

[[machinelearning_mit.epub]]

[[thetechnologicalsingularity.epub]]
