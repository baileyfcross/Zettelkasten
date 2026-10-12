2026-10-12 01:15

Status: #baby

Tags: [[Quantum Autoencoding and State Compression]]

# Quantum Autoencoder Latent Rank Condition

A quantum autoencoder can exactly represent the support of an input density operator only when its latent Hilbert space is large enough. For a (K)-qubit latent register and an input of rank (r), the basic capacity condition is (2^K \geq r).

This condition explains why the paper focuses on low-rank states. Their support may fit into a register much smaller than the original (N)-qubit system, so [[Quantum Autoencoder Spectral Preservation]] can make latent-state tomography substantially cheaper. If the rank exceeds the latent dimension, distinct supported directions must compete for insufficient capacity and information is necessarily lost.

Increasing (K) can improve compression, but it also reduces the dimensional savings. The useful regime therefore lies between under-capacity, which creates large [[Quantum Autoencoder Reconstruction Error]], and a latent register so large that compression no longer offers much benefit.

# References

[[2021 - On exploring practical potentials of quantum auto-encoder with advantages.pdf]]
