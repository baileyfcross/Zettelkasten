2026-10-12 01:15

Status: #baby

Tags: [[Quantum Autoencoding and State Compression]]

# Quantum Autoencoder Reconstruction Error

Quantum autoencoder reconstruction error measures how far the decoded approximation is from the original quantum state. The paper expresses this discrepancy through a fidelity-derived quantity: when the fidelity between the original state and its reconstruction is close to one, the reconstruction error is small.

This error connects imperfect compression to the reliability of later calculations. Bounds for [[QAE-Based Low-Rank Fidelity Estimation]], [[QAE-Based Quantum Fisher Information Estimation]], and [[QAE-Based Gibbs State Preparation]] all contain a term determined by the quality of reconstruction. The learned representation is therefore not merely an intermediate artifact; its measured error becomes part of the guarantee for the downstream result.

Training loss and reconstruction error are related because both reflect information left outside the intended latent subspace, but they are not interchangeable descriptions. Training loss is the variational objective applied to the encoded trash subsystem, whereas reconstruction error compares the original state with the state produced after compression and decoding.

# References

[[2021 - On exploring practical potentials of quantum auto-encoder with advantages.pdf]]
