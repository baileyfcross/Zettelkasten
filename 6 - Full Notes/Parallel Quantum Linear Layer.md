2026-10-15 00:05

Status: #baby

Tags: [[Quantum and Hybrid Convolutional Image Classification]]

# Parallel Quantum Linear Layer

A parallel quantum linear layer divides a classical input vector into chunks and assigns each chunk to an independent parameterized quantum circuit. Measuring the circuits produces an output vector analogous to a classical linear layer, although its width is constrained by the number of measured qubits and the selected encoding.

The layer exposes a resource tradeoff. More qubits in each circuit let one circuit model correlations across a larger feature group, while more small circuits reduce the qubit requirement per device and can run concurrently. In the paper's fixed 768-feature interface, one-feature-per-qubit encodings use 96 circuits, whereas amplitude encoding compresses the same input into three circuits. Independence makes circuit-level parallelism possible, but it also means that correlations crossing chunk boundaries are unavailable unless earlier classical layers have already combined them.

# References

[[2025 - Practical insights on the effect of different encodings ansatze and measurements in quantum and hybrid convolutional neural networks.pdf]]
