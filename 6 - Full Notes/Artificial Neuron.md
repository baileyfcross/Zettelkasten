2026-09-05 16:28

Status: #baby

Tags: [[Artificial Neural Network Structure]]

# Artificial Neuron

An artificial neuron computes a weighted combination of its inputs, adds a bias, and passes the result through an activation function. The output becomes an input to units in the next layer.

Although loosely inspired by biology, the artificial neuron is a mathematical building block. Its weights are learned through procedures such as [[Backpropagation]] rather than specified as symbolic rules.

More precisely, each input is multiplied by a [[Neural Network Weight]], the products form a [[Weighted Input]], and a [[Neural Network Bias]] shifts that value before an [[Activation Function]] calculates the output. This makes the unit a small parameterized computation that can be simulated in ordinary software; no literal artificial cell is required.

Kelleher's two-stage view distinguishes the weighted sum from the nonlinear activation applied afterward. A unit's output can be a final prediction or an intermediate learned feature passed to later units. He also shows that the bias can be represented as a weight on a constant input of one, making its calculation and training part of the same weighted-input structure.

# References

[[aiassistants.epub]]

[[algorithms.epub]]

[[deeplearning_mit.epub]]
