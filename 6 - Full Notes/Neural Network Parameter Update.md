2026-09-06 00:13

Status: #baby

Tags: [[Optimization and Differentiation]]

# Neural Network Parameter Update

A neural-network parameter update changes weights and biases so that future predictions produce a smaller [[Loss Function|loss]]. For each parameter, training calculates how the loss changes and moves the value a small amount in the opposite direction.

The [[Gradient]] gathers these local changes for all parameters. [[Backpropagation]] makes the required derivative information available from the output layer back through the earlier layers, and a [[Neural Network Optimizer]] controls how the updates are applied.

Kelleher distinguishes the gradient-calculation step from the update rule. For a connection weight, the error sensitivity computed at its destination neuron is combined with the activation received from its source neuron; [[Gradient Descent]] then changes that weight by a [[Learning Rate|learning-rate-scaled]] step in the loss-reducing direction. Backpropagation supplies the sensitivity, but it is not itself the only possible choice of weight-update rule.

# References

[[algorithms.epub]]

[[deeplearning_mit.epub]]
