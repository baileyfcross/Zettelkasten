2026-10-12 01:15

Status: #baby

Tags: [[Quantum Autoencoding and State Compression]]

# Quantum Autoencoder Spectral Preservation

An optimally trained [[Quantum Autoencoder]] can preserve the nonzero spectrum of a low-rank input state in its compressed latent state. When the latent Hilbert space is large enough to contain the input's support, the encoder changes the representation of that support without changing its eigenvalues.

This property makes compression useful for more than reconstructing the state. Tomography can be performed on the smaller (K)-qubit latent register, after which classical diagonalization yields its eigenvalues and latent eigenvectors. Appending the reference trash state and applying the inverse encoder lifts those latent eigenvectors back into the original (N)-qubit space.

The procedure therefore provides access to the spectral information of a large low-rank state through a smaller quantum system. The statement depends on optimal compression and sufficient latent capacity; outside those conditions, the compressed spectrum is an approximation whose reliability must be assessed through [[Quantum Autoencoder Reconstruction Error]].

# References

[[2021 - On exploring practical potentials of quantum auto-encoder with advantages.pdf]]
