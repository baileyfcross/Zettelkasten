2026-09-06 21:47

Status: #baby

Tags: [[Probabilistic Robotics and Decision Models]] · [[Reinforcement Learning Methods]]

# Partially Observable Markov Decision Process

A partially observable Markov decision process extends a Markov decision process with hidden states and probabilistic observations. The decision-maker therefore maintains a belief distribution rather than acting from a perfectly known state.

Each action affects both future rewards and the information available through later observations. A policy maps beliefs to actions, coupling recursive state estimation with sequential decision-making.

When an agent receives a sensor observation rather than the state itself, it can update all plausible states weighted by their probabilities. This additional inference makes value learning harder because identical observations may represent different situations that call for different actions.

# References

[[bayesianprogramming.pdf]]

[[machinelearning_mit.epub]]
