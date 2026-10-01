2026-09-30 21:11

Status: #baby

Tags: [[Reinforcement Learning Methods]]

# Value Network

A value network is a regressor that estimates the expected cumulative reward available from a game or environment state. It compresses many possible future sequences into a score indicating how promising the current situation is.

Because the final reward may arrive only after many moves, the training target is propagated backward through experience rather than supplied directly for every state. A [[Policy Network]] can use value estimates to prefer actions that lead toward more valuable successor states.

# References

[[machinelearning_mit.epub]]
