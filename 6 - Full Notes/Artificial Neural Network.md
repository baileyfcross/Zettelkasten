2026-09-05 16:28

Status: #baby

Tags: [[Artificial Neural Network Structure]]

# Artificial Neural Network

An artificial neural network is a parameterized network of simple computational units arranged in connected layers. Each unit combines weighted inputs, applies a nonlinear function, and passes its output onward.

Learning changes the connection weights so that the network maps inputs to useful outputs. Multiple layers form a [[Deep Neural Network]], while specialized connections support sequence and spatial processing.

Networks commonly arrange neurons into an input layer, one or more [[Hidden Layer|hidden layers]], and an output layer. A [[Dense Layer]] connects every unit to every neuron in the following layer, though other connection patterns can be chosen for different tasks. [[Forward Propagation]] carries activations toward the output, and [[Backpropagation]] sends parameter-adjustment information in the reverse direction during training.

Kelleher emphasizes that each processing neuron performs two steps: a weighted sum of incoming values and an [[Activation Function]] applied to that sum. The network's function is built by [[Neural Model Composition|composing]] those small transformations. For a fully connected layer, the sums can be evaluated together as [[Layer Matrix Computation|vector–matrix multiplication]], with nonlinear activations applied afterward. This mathematical regularity helps explain the suitability of GPU-style matrix hardware for repeated network runs.

# References

[[aiassistants.epub]]

[[algorithms.epub]]

[[deeplearning_mit.epub]]
