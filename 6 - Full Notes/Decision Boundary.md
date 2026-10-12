2026-09-06 00:13

Status: #baby

Tags: [[Neural Network Training]]

# Decision Boundary

A decision boundary separates the regions of input space that a [[Classifier]] assigns to different outcomes. In two dimensions it can be visualized as a line or curve between classes.

A single [[Perceptron]] can learn only a linear boundary, so it handles data that can be divided by one straight line. An [[Artificial Neural Network]] with hidden layers can combine neuron outputs to represent more complicated, nonlinear boundaries.

Kelleher's two-input threshold-neuron example makes the geometry concrete. The boundary is perpendicular to the neuron's input-weight vector; altering the weights rotates it, while a [[Neural Network Bias|bias term]] moves it off the origin. That separates the effects of weight direction and threshold position on which [[Model Input Space|input points]] receive high activation.

# References

[[algorithms.epub]]

[[deeplearning_mit.epub]]
