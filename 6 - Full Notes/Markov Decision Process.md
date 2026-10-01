2026-09-06 21:47

Status: #baby

Tags: [[Probabilistic Robotics and Decision Models]] · [[Reinforcement Learning Methods]]

# Markov Decision Process

A Markov decision process combines probabilistic state transitions with actions and rewards. A policy specifies how actions are selected so that expected cumulative reward is optimized over time.

The Markov assumption makes the next state depend on the current state and action rather than the entire history. When the current state is not directly known, decisions must instead operate on a belief distribution.

Actions can produce uncertain next states and rewards because of hidden environmental factors, imperfect sensing, or other agents. Reinforcement learning estimates action values over repeated trials and uses a [[Bellman Reward Backup]] to connect an immediate transition with the discounted value of later states.

# References

[[bayesianprogramming.pdf]]

[[machinelearning_mit.epub]]
