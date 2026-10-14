2026-10-14 17:27

Status: #baby

Tags: [[Unary-Encoded Quantum Neural Networks]]

# Quantum-Assisted Neural Network

A quantum-assisted neural network retains a classical fully connected architecture and classical weight representation while replacing selected data-weight dot products with [[Signed Quantum Inner-Product Estimation|quantum inner-product estimates]]. Both inference and backpropagation can call the quantum subroutine; gradient descent and the network's hypothesis family remain classical.

This design is therefore different from a generic variational quantum classifier. Its quantum circuit is an arithmetic coprocessor whose finite-shot output introduces estimation noise into an otherwise ordinary neural network. A parallel loader gives an ideal per-sample circuit depth of $O(\log d)$ for $d$ features, subject to the [[Shot Complexity of Quantum Inner-Product Estimation]] and the availability of sufficient qubits and connectivity.

# References

[[2022 - Quantum Methods for Neural Networks and Application to Medical Image Classification.pdf]]
