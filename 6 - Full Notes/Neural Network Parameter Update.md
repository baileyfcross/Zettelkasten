2026-09-06 00:13

Status: #baby

Tags: [[Optimization and Differentiation]]

# Neural Network Parameter Update

A neural-network parameter update changes weights and biases so that future predictions produce a smaller [[Loss Function|loss]]. For each parameter, training calculates how the loss changes and moves the value a small amount in the opposite direction.

The [[Gradient]] gathers these local changes for all parameters. [[Backpropagation]] makes the required derivative information available from the output layer back through the earlier layers, and a [[Neural Network Optimizer]] controls how the updates are applied.

# References

[[algorithms.epub]]
