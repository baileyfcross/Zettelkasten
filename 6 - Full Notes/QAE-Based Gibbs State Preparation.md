2026-10-12 01:15

Status: #baby

Tags: [[Quantum Autoencoding and State Compression]]

# QAE-Based Gibbs State Preparation

QAE-based Gibbs state preparation is a variational method that trains a parameterized mixed state by minimizing free energy. The energy term is obtained from Hamiltonian expectation values, while a [[Quantum Autoencoder]] compresses the trial state so its eigenvalues can be used to calculate von Neumann entropy.

This spectral route avoids replacing entropy with a truncated Taylor expansion. The variational circuit is adjusted until the energy-entropy balance approaches that of the target thermal state at the chosen inverse temperature. The paper demonstrates the method numerically on a three-qubit Ising chain at several temperatures and reports high final fidelities in those simulations.

The accompanying bound relates fidelity with the desired Gibbs state to the free-energy gap and to compression quality. Consequently, success depends on both the outer free-energy optimization and low [[Quantum Autoencoder Reconstruction Error]]. The simulations support feasibility on small systems, but they do not constitute a hardware demonstration or an unconditional scaling advantage.

# References

[[2021 - On exploring practical potentials of quantum auto-encoder with advantages.pdf]]
