2026-10-15 00:05

Status: #baby

Tags: [[Quantum and Hybrid Convolutional Image Classification]]

# HQNN-Quanvolution Architecture

HQNN-Quanvolution places its quantum component at the front of an image network. It replaces the first classical convolution with parameter-tied quantum patch circuits, applies a fixed ReLU to their measured outputs, and then passes the resulting feature maps through classical convolutions, global averaging, and fully connected classification layers.

Each RGB channel is processed independently with overlapping $2\times2$ or $3\times3$ patches at stride one. A patch of side $qks$ is flattened and encoded into $qks^2$ qubits, followed by two repeated ansatz blocks and one measurement per qubit. Unlike [[HQNN-Parallel Quantum-Later Architecture]], this design asks the circuit to discover useful structure directly from local pixels. In the reported simulations, its best configurations approached but did not exceed the structural-twin classical convolutional baseline.

# References

[[2025 - Practical insights on the effect of different encodings ansatze and measurements in quantum and hybrid convolutional neural networks.pdf]]
