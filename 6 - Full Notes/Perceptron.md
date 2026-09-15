2026-09-06 00:13

Status: #baby

Tags: [[Artificial Neural Network Structure]] · [[Neural Network Classification and Clustering]]

# Perceptron

A Perceptron is an [[Artificial Neuron]] whose activation is a step function. It outputs one when its weighted input and bias cross the threshold and zero otherwise.

A single Perceptron can learn a linear [[Decision Boundary]] and separate two classes when the observations are linearly separable. More complicated boundaries require networks that combine multiple neurons in connected layers.

In the book's classification treatment, a perceptron has input nodes fully connected to class outputs, combines inputs through weights, and applies an activation function. Its learning rule can find a linear separator when one exists; the XOR example demonstrates why nonlinear problems require hidden layers and a multilayer network.

Kelleher describes Rosenblatt's rule as error correction after each labeled example: if the output is correct the weights remain unchanged; otherwise, weights are changed in a direction intended to correct the mistake. The [[Learning Rate]] scales those changes. The convergence result applies when a separating set of weights exists, but an unsuccessful long run alone cannot tell whether convergence is merely slow or impossible for the examples.

# References

[[algorithms.epub]]

[[clusteranalysisanddatamining.pdf]]

[[deeplearning_mit.epub]]
