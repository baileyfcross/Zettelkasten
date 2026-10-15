2026-10-15 00:05

Status: #baby

Tags: [[Quantum and Hybrid Convolutional Image Classification]]

# Shaped Embedding Quantum Neural Network

A shaped embedding quantum neural network isolates the effect of pixel ordering in an amplitude-encoded image classifier. Its two-kernel form applies arbitrary two-qubit unitaries to two adjacent qubit pairs, traces out one qubit from each pair as pooling, and sends the remaining register through a simplified fully connected quantum layer before measurement.

The paper compares this structure with a baseline containing only the fully connected quantum layer and with a deeper [[Quantum Convolutional Neural Network]]. Each is evaluated under random and spatially designed amplitude orderings. Because even the nominal fully connected layer is built from adjacent two-qubit gates, it also responds to ordering; the two-kernel model makes that dependence easiest to interpret. The experiment tests whether useful locality can be created through the embedding map without adding a classical image-feature extractor.

# References

[[2025 - Practical insights on the effect of different encodings ansatze and measurements in quantum and hybrid convolutional neural networks.pdf]]
