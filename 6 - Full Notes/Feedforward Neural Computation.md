2026-09-13 10:30

Status: #baby

Tags: [[Neural Network Classification and Clustering]]

# Feedforward Neural Computation

Feedforward neural computation passes input values through weighted sums and activation functions from the input layer toward the output layer without sending values backward during prediction.

Each layer's output becomes the next layer's input. During training, a separate backward pass uses the resulting error to calculate weight updates.

Kelleher represents a dense feedforward network as a chain of [[Layer Matrix Computation|matrix multiplications]] with elementwise nonlinear activations between them. This expresses the same computations as a diagram of connected neurons but makes the repeated weighted-sum work more suitable for matrix-oriented hardware.

# References

[[clusteranalysisanddatamining.pdf]]

[[deeplearning_mit.epub]]
