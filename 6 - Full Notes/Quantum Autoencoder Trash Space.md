2026-10-12 01:15

Status: #baby

Tags: [[Quantum Autoencoding and State Compression]]

# Quantum Autoencoder Trash Space

The trash space of a [[Quantum Autoencoder]] is the (N-K)-qubit subsystem that the encoder is trained to make redundant. A successful encoder concentrates the relevant information in the (K)-qubit latent subsystem while mapping the trash subsystem toward a known reference such as the all-zero state.

Training loss measures how much encoded probability remains outside the subspace in which every trash qubit has the desired value. Minimizing that loss therefore supplies an operational criterion for compression: the closer the trash register is to its reference, the less information should be lost when it is discarded.

The name does not mean that these qubits are irrelevant before training. They become disposable only after the learned unitary has relocated the recoverable structure into the latent register. A poor optimization result leaves information in the trash subsystem, which appears later as [[Quantum Autoencoder Reconstruction Error]].

# References

[[2021 - On exploring practical potentials of quantum auto-encoder with advantages.pdf]]
