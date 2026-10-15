2026-10-15 10:16

Status: #baby

Tags: [[A-qGAN Anomaly Detection in High-Energy Physics]]

# Anomaly qGAN Framework

An anomaly quantum generative adversarial network, or A-qGAN, learns a reference distribution from Standard Model collision events encoded as quantum states. Its quantum generator approximates the background distribution, while its quantum discriminator learns to distinguish embedded training events from the generator's state. After training, events that do not conform to the learned reference receive a distinct anomaly score.

The training objective is unsupervised with respect to a particular beyond-Standard-Model signal: the generative model is fitted to background events rather than to labeled examples of every possible new particle. This makes the framework suitable for model-agnostic searches in which the form of an anomaly is not known beforehand.

The proof-of-principle evaluation nevertheless uses held-out Higgs and Graviton samples to select score settings and measure discrimination. This separates an unsupervised representation-learning stage from a labeled benchmarking and calibration stage. The core mechanism is detailed by [[qGAN Quantum-State Distribution Learning]] and [[A-qGAN Composite Anomaly Score]].

# References

[[2023 - Quantum Generative Adversarial Networks For Anomaly Detection In High Energy Physics.pdf]]
