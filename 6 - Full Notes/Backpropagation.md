2026-09-05 16:28

Status: #baby

Tags: [[Neural Network Training]]

# Backpropagation

Backpropagation is the procedure used to calculate how much each neural-network parameter contributed to an output error. It propagates error information backward through the network using the chain rule.

An optimizer uses those gradients to adjust weights toward lower error over many training examples. This makes it possible to train multilayer [[Artificial Neural Network|neural networks]] as coordinated systems.

Training first uses [[Forward Propagation]] to calculate layer-by-layer activations and the final loss. Backpropagation then works from the output toward the input, calculating how weights and biases in each layer affect that loss. These derivatives support a [[Neural Network Parameter Update]] across the entire network.

# References

[[aiassistants.epub]]

[[algorithms.epub]]
