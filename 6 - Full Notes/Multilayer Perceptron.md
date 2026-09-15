2026-09-13 10:30

Status: #baby

Tags: [[Neural Network Classification and Clustering]]

# Multilayer Perceptron

A multilayer perceptron contains an input layer, one or more hidden layers, and an output layer with weighted connections between adjacent layers. Nonlinear activations let the network represent relationships that are not linearly separable.

Feedforward computation produces predictions, while backpropagation and gradient descent adjust weights to reduce an error function.

Kelleher uses the transition from one-layer [[Perceptron|perceptrons]] to multilayer networks to explain the importance of hidden-unit credit assignment. [[Backpropagation]] can train those hidden weights when the network has activation functions with usable derivatives. Nonlinear layers overcome the one-line boundary limit illustrated by [[XOR Classification Problem|XOR]], though deep stacks also raise the [[Vanishing Gradient Problem|vanishing-gradient]] challenge.

# References

[[clusteranalysisanddatamining.pdf]]

[[deeplearning_mit.epub]]
