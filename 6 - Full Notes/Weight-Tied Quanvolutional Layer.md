2026-10-15 00:05

Status: #baby

Tags: [[Quantum and Hybrid Convolutional Image Classification]]

# Weight-Tied Quanvolutional Layer

A weight-tied quanvolutional layer reuses one parameterized quantum circuit at every image-patch position and color channel. The shared rotation angles play the role of a convolutional filter, while measuring every qubit yields several scalar feature maps for each input channel. This is the quantum analogue of [[Convolutional Weight Sharing]] rather than a collection of separately trained patch circuits.

Parameter sharing keeps the number of quantum trainable weights fixed as image resolution or stride changes. In the studied implementation, the quantum parameter count is only a few hundred and is roughly 10 to 100 times smaller than a classical first convolution producing the same number of channels. That compactness does not guarantee lower execution cost: each overlapping patch still requires a circuit evaluation, and simulating larger patches becomes prohibitive as the qubit count grows quadratically with the patch side.

# References

[[2025 - Practical insights on the effect of different encodings ansatze and measurements in quantum and hybrid convolutional neural networks.pdf]]
