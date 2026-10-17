2026-10-16 17:54

Status: #baby

Tags: [[Variational Quantum Wasserstein Anomaly Detection]]

# Quantum AnoGAN Identity-Block Initialization

Identity-block initialization pairs a randomly initialized circuit layer with its complex conjugate so the block initially evaluates to the identity. It is intended to begin optimization in a shallow, non-random regime where gradient variance has not yet collapsed as it can in a [[Barren Plateau Gradient Scaling|barren plateau]].

On the nine-qubit fraud task, this initialization does not improve the quantum AnoGAN's final F1 score and makes some depth-three circuits slightly worse. The local cost, shallow depth, and small register already reduce the expectation of a barren plateau, so the mitigation has little room to help in this experiment.

The negative result is architecture-specific rather than evidence against identity initialization in general. With a one-layer block, pairing layers can also remove an entangling layer relative to a randomly initialized circuit of the same nominal depth, changing capacity as well as initialization. Noise-induced plateaus are outside the study because the simulations are noiseless.

# References

[[2021 - Anomaly detection with variational quantum generative adversarial networks.pdf]]
