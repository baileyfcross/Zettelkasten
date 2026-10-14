2026-10-14 17:27

Status: #baby

Tags: [[Unary-Encoded Quantum Neural Networks]]

# Quantum Orthogonal Neural Network

A quantum orthogonal neural network uses a [[Quantum Pyramidal Circuit]] as a trainable linear layer. [[Unary Amplitude Encoding]] restricts the circuit to an $n$-dimensional subspace, where the gates implement an exactly orthogonal weight matrix rather than an arbitrary transformation over the full $2^n$-dimensional Hilbert space.

The model trains RBS angles directly with [[RBS Angle-Space Backpropagation]] instead of updating matrix elements and then repairing orthogonality. This gives a distinct optimization landscape while preserving vector norms and controlling the relationship to a classical orthogonal network. Its quantum forward pass still requires [[Signed Unary-State Tomography]] before a classical activation function can connect it to another layer.

# References

[[2022 - Quantum Methods for Neural Networks and Application to Medical Image Classification.pdf]]
