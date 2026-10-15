2026-10-12 01:33

Status: #baby

Tags: [[Enhanced Feature Quantum Autoencoders]]

# QAE Local Cost Depolarizing-Noise Resilience

The [[Local Trash-Qubit Compression Cost]] has the same minimizing parameters under the paper's model of global depolarizing noise as it does without that noise. At circuit depth (D), depolarization scales each measured Pauli-Z expectation by a common positive factor, so maximizing their sum selects the same parameters.

This is a statement about the location of the optimum, not a claim that noise leaves measurements or reconstructed states unchanged. The observed cost is shifted and its signal can still be weakened; the derivation only shows that the ideal and noisy objectives have the same argmin under the specified global depolarizing channel.

This is an instance of [[Optimal Parameter Resilience Is Not Trainability]]. Uniform depolarizing contraction can preserve the preferred parameters while reducing the separation between their cost and nearby alternatives, so finite-shot optimization may still require substantially more measurements.

The result is also model-specific. It does not establish resilience to arbitrary local, correlated, coherent, or hardware-dependent errors. Its value is that the local objective used by the enhanced feature autoencoder retains its preferred parameters under one analytically tractable noise process.

# References

[[2021 - Quantum autoencoders with enhanced data encoding.pdf]]

[[2021 - Can Error Mitigation Improve Trainability of Noisy Variational Quantum Algorithms.pdf]]
