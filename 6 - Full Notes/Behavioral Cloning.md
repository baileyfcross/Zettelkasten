2026-09-30 21:11

Status: #baby

Tags: [[Reinforcement Learning Methods]]

# Behavioral Cloning

Behavioral cloning records the action a demonstrator takes in each observed state and trains a model to reproduce that mapping with [[Supervised Learning]]. A driving dataset, for example, can pair road and traffic situations with an expert driver's control actions.

The method converts one sequential task into many labeled state-action examples and can provide a useful starting policy without blind exploration. It learns the visible behavior rather than the underlying reward, so its reliability depends on the demonstrations covering situations the cloned policy will encounter.

# References

[[machinelearning_mit.epub]]
