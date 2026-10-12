2026-10-12 01:33

Status: #baby

Tags: [[Enhanced Feature Quantum Autoencoders]]

# Enhanced Feature Quantum Autoencoder

An enhanced feature quantum autoencoder, or EF-QAE, is a [[Quantum Autoencoder]] whose encoder depends on both learned parameters and a feature vector describing the input model. Instead of applying one fixed learned unitary to every state, it applies a family of related unitaries selected by the supplied features.

The feature dependence lets compression adapt to systematic differences among states while the learned parameters capture structure shared across the training set. The decoder applies the inverse feature-conditioned unitary to the latent state and a reference trash register, seeking to recover the original state with higher fidelity.

In the paper's simulations, this design improves compression over a standard QAE at the same circuit depth for Ising-model ground states and amplitude-encoded handwritten digits. The result is a tradeoff rather than a free improvement: [[EF-QAE Classical Optimization Tradeoff]] explains why the enhanced model can require more trainable parameters and classical optimization.

# References

[[2021 - Quantum autoencoders with enhanced data encoding.pdf]]
