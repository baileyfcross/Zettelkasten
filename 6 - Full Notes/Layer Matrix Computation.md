2026-09-15 02:20

Status: #baby

Tags: [[Artificial Neural Network Structure]]

# Layer Matrix Computation

The weighted sums for a fully connected neural-network layer can be calculated together. Put the preceding layer's activations in a vector and the connection weights in a matrix; their product produces a vector of weighted sums for the next layer's neurons. An [[Activation Function]] is then applied element by element.

This is the matrix view of [[Feedforward Neural Computation]]. It replaces many separately described neuron calculations with one structured operation, while preserving the same connections. Kelleher uses the view to explain why matrix-oriented hardware can accelerate repeated forward and training passes through a network.

# References

[[deeplearning_mit.epub]]
