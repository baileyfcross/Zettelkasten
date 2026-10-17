2026-10-16 23:00

Status: #baby

Tags: [[Quantum Invertible Generative Models]]

# Learnable Hybrid Inverse State Preparation

Learnable hybrid inverse state preparation maps a measured QINN output back to a quantum state suitable for running the main circuit in reverse. A small classical network first predicts three rotation angles for every qubit. Those rotations prepare a product state, and a separate variational quantum circuit further transforms it into the reconstructed premeasurement state.

This module is used only in the inverse path. Training it jointly with the forward circuit lets the model shape both the reachable output-state manifold and the rule that returns measured values to that manifold.

A learned module is less restrictive than fixing one analytic inverse preparation for every possible forward circuit. Its adequacy can be judged by exact state overlap through [[SWAP-Test State-Fidelity Invertibility Loss]] or by functional input reconstruction through [[Reconstruction MSE Invertibility Loss]].

# References

[[2023 - Generative Invertible Quantum Neural Networks.pdf]]

