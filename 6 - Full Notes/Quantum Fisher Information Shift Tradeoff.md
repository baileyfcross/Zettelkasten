2026-10-12 01:15

Status: #baby

Tags: [[Quantum Autoencoding and State Compression]]

# Quantum Fisher Information Shift Tradeoff

Finite-difference quantum Fisher information estimation uses the fidelity between states generated at parameter values separated by a small shift. Reducing the shift improves the local approximation on which the estimator is based, but it also amplifies error inherited from imperfect quantum-autoencoder reconstruction.

In the bound derived for [[QAE-Based Quantum Fisher Information Estimation]], the compression-dependent contribution grows inversely with the square of the parameter shift. A very small shift can therefore make even modest [[Quantum Autoencoder Reconstruction Error]] dominate the result.

The shift must be selected as a compromise rather than simply minimized. It needs to be small enough to represent local parameter sensitivity while remaining large enough that fidelity-estimation and compression errors do not overwhelm the finite difference. Better autoencoder training relaxes this constraint by reducing the reconstruction term.

# References

[[2021 - On exploring practical potentials of quantum auto-encoder with advantages.pdf]]
