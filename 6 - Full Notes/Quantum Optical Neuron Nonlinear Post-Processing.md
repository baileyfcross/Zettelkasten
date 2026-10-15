2026-10-14 18:20

Status: #baby

Tags: [[Quantum Optical Neurons]]

# Quantum Optical Neuron Nonlinear Post-Processing

The optical overlap measurement already introduces a nonlinearity through the squared magnitude $|\langle I,U\rangle|^2$. The classifier strengthens and calibrates that response by adding a trainable bias and applying a [[Sigmoid Activation Function]]. The resulting scalar is interpreted as a binary class probability and can be trained with binary cross-entropy.

The bias also compensates heuristically for normalization changes caused by optical losses, which can lower the norm factor in the coincidence equation. An ablation in the paper shows why the post-processing matters: using only the square-magnitude response still trains, but its asymptotic accuracy falls to about 88% for MNIST zero-versus-one and 57% for CIFAR-10 cat-versus-dog, compared with above 99% and 58% for the full simulated model. The electronic work remains scalar rather than scaling with image resolution.

# References

[[2024 - Quantum optical classifier with superexponential speedup.pdf]]
