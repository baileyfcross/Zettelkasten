2026-09-15 02:14

Status: #baby

Tags: [[Convolutional Visual Architecture]]

# Convolutional Feature Map

A feature map records the output of one [[Convolutional Kernel]] at each location where the kernel is applied. It is a spatial account of how strongly the learned local detector responded across an image, not merely a single yes-or-no answer for the whole image.

A nonlinear [[Activation Function]] is commonly applied element by element to the map before a [[CNN Pooling Layer]] downsamples it. Maps from different kernels can also be combined and passed to a later convolutional layer. This lets the network build features from earlier detections while preserving spatial information until the architecture chooses to reduce it.

# References

[[deeplearning_mit.epub]]
