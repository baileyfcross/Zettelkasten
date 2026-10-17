2026-10-16 22:03

Status: #baby

Tags: [[Variational Quantum Wasserstein Anomaly Detection]] · [[Experimental Quantum GAN Image Generation]]

# Quantum Latent Rotation Encoding

The hybrid generator encodes each latent coordinate $z_i\in[-\pi,\pi]$ with an $R_X(z_i)$ rotation on one qubit. The state-preparation circuit therefore maps an $N$-dimensional uniformly sampled latent vector into an $N$-qubit product state before the trainable circuit introduces additional rotations and, in most tested ansatze, entanglement.

This is latent-data encoding rather than loading the observed transaction. During adversarial training, high-dimensional records are sent directly to the classical critic, while the quantum circuit processes only random variables whose dimension equals the qubit count. During anomaly scoring, the same preparation angles become the variables optimized by [[AnoGAN Latent Variable Optimization]].

One-coordinate-per-qubit rotation encoding is shallow and compatible with small devices, but it does not compress an arbitrary classical record into logarithmically many qubits. The practical advantage claimed for the design is avoidance of high-dimensional quantum data preparation, not an asymptotic encoding speedup.

The image-generation patch qGAN uses the same pattern with $R_Y$ rotations whose angles are sampled from a chosen latent distribution. Every patch sub-generator receives the same latent state during an iteration so their probability vectors form one image drawn from a single generator map. Here the rotations encode random generator input, while amplitude encoding of real images is reserved for the distinct quantum batch architecture.

The style-qGAN deliberately extends this one-time encoding pattern. Instead of confining the latent variables to state preparation, it supplies affine functions of them to single-qubit and entangling gates throughout the circuit. [[Style-qGAN Latent Reuploading]] uses the repeated access to enlarge the attainable feature-map family while preserving the standard generator as a special case.

# References

[[2021 - Anomaly detection with variational quantum generative adversarial networks.pdf]]

[[2021 - Experimental Quantum Generative Adversarial Networks for Image Generation.pdf]]

[[2022 - Style-based quantum generative adversarial networks for Monte Carlo events.pdf]]
