2026-09-06 00:13

Status: #baby

Tags: [[Artificial Neural Network Structure]]

# Rectifier Activation Function

The rectifier activation function maps every negative input to zero and returns positive input in direct proportion to its value. A neuron using this function is called a rectified linear unit, or ReLU.

Unlike sigmoid and tanh, the positive side does not flatten toward a fixed maximum. Different neural architectures favor different [[Activation Function|activation functions]], and ReLU units are common building blocks in deep networks.

Kelleher emphasizes the training tradeoff: the rectifier's derivative is one on its positive side, letting gradients pass through active units without the repeated shrinkage of a saturated sigmoid. Its negative side has zero gradient, however, so inactive units do not train from that local signal. A leaky variant introduces a nonzero negative-side slope. The activation choice affects both representational behavior and the [[Vanishing Gradient Problem|flow of training gradients]].

# References

[[algorithms.epub]]

[[deeplearning_mit.epub]]
