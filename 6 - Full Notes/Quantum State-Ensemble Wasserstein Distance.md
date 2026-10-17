2026-10-16 23:13

Status: #baby

Tags: [[Quantum State Diffusion Models]]

# Quantum State-Ensemble Wasserstein Distance

A Wasserstein distance compares quantum-state distributions by finding an optimal transport plan between their samples. For pure states, the paper uses an infidelity-based cost derived from

$$D^2(|\phi\rangle,|\psi\rangle)=1-|\langle\phi|\psi\rangle|^2.$$

For finite ensembles, the transport problem becomes a linear program whose row and column constraints reproduce the two empirical distributions. Unlike fidelity-kernel MMD, the resulting metric is identifiable: it is zero only when the two distributions agree.

This geometric sensitivity matters for nontrivial support. The Wasserstein loss detects the progressive scrambling of a one-qubit ring and guides its reverse denoising, while the fidelity-kernel MMD is exactly zero between that ring and Haar noise.

# References

[[2023 - Generative quantum machine learning via denoising diffusion probabilistic models.pdf]]

