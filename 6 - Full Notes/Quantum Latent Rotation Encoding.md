2026-10-16 17:54

Status: #baby

Tags: [[Variational Quantum Wasserstein Anomaly Detection]]

# Quantum Latent Rotation Encoding

The hybrid generator encodes each latent coordinate $z_i\in[-\pi,\pi]$ with an $R_X(z_i)$ rotation on one qubit. The state-preparation circuit therefore maps an $N$-dimensional uniformly sampled latent vector into an $N$-qubit product state before the trainable circuit introduces additional rotations and, in most tested ansatze, entanglement.

This is latent-data encoding rather than loading the observed transaction. During adversarial training, high-dimensional records are sent directly to the classical critic, while the quantum circuit processes only random variables whose dimension equals the qubit count. During anomaly scoring, the same preparation angles become the variables optimized by [[AnoGAN Latent Variable Optimization]].

One-coordinate-per-qubit rotation encoding is shallow and compatible with small devices, but it does not compress an arbitrary classical record into logarithmically many qubits. The practical advantage claimed for the design is avoidance of high-dimensional quantum data preparation, not an asymptotic encoding speedup.

# References

[[2021 - Anomaly detection with variational quantum generative adversarial networks.pdf]]
