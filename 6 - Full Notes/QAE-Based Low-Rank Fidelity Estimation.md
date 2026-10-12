2026-10-12 01:15

Status: #baby

Tags: [[Quantum Autoencoding and State Compression]]

# QAE-Based Low-Rank Fidelity Estimation

QAE-based low-rank fidelity estimation uses a [[Quantum Autoencoder]] to estimate the fidelity between a low-rank quantum state and another state. The autoencoder first compresses the low-rank state, allowing tomography and diagonalization to be performed on the smaller latent register rather than directly on the full system.

The latent eigenvectors can be lifted back into the original space with the inverse encoder. Overlaps between those reconstructed eigenvectors and the comparison state are then estimated with SWAP-test variants and assembled into a smaller matrix whose trace supplies the fidelity estimate.

The estimate is accompanied by a bound controlled by [[Quantum Autoencoder Reconstruction Error]]. Simulations in the paper show that larger latent spaces reduce training loss and tighten the estimate for low-rank inputs. Full-rank inputs do not receive the same benefit unless the latent register approaches the size of the original system, illustrating the importance of the [[Quantum Autoencoder Latent Rank Condition]].

# References

[[2021 - On exploring practical potentials of quantum auto-encoder with advantages.pdf]]
