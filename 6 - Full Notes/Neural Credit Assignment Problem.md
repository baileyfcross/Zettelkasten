2026-09-15 02:20

Status: #baby

Tags: [[Neural Network Training]]

# Neural Credit Assignment Problem

In a multilayer network, the training data specify an expected final output, not the correct activation for each hidden neuron. Credit assignment asks how much each hidden unit and weight contributed to the network's output error so that parameter changes can be directed appropriately.

[[Backpropagation]] addresses the problem by calculating local error gradients at the output and propagating them backward through the connections. A [[Gradient Descent|weight-update method]] can then use the resulting derivatives. Kelleher distinguishes these steps: assigning sensitivity to internal parameters is necessary before choosing how to change those parameters.

# References

[[deeplearning_mit.epub]]
