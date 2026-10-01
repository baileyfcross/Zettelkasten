2026-09-30 21:11

Status: #baby

Tags: [[Reinforcement Learning Methods]]

# Policy Network

A policy network maps an observed state or state representation to a choice among available actions. It acts like a classifier whose output is an action, but its training objective is the long-run reward created by a sequence of choices rather than a teacher-provided label at each step.

In game systems, a policy network can select a move while a [[Value Network]] estimates how close the resulting position is to eventual success. Combining learned policy and value information narrows search toward choices that are both plausible and promising.

# References

[[machinelearning_mit.epub]]
