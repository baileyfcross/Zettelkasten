2026-10-12 01:33

Status: #baby

Tags: [[Enhanced Feature Quantum Autoencoders]]

# Local Trash-Qubit Compression Cost

A local trash-qubit compression cost measures how closely each discarded qubit approaches the desired zero state after encoding. It can be written as an average of local Pauli-Z expectations, or estimated from measurement outcomes by penalizing their [[Hamming Distance]] from the all-zero bit string.

The cost reaches zero exactly when every trash qubit is in the desired zero configuration. This connects the training objective directly to the decoupling interpretation of [[Quantum Autoencoder Trash Space]]: if the trash subsystem is fixed and pure, it can be discarded without retaining information about the latent subsystem.

Using local observables also avoids the paper's concern that global fidelity-based objectives can become difficult to train even for shallow circuits. The resulting objective is both a compression diagnostic and the basis for the limited noise result in [[QAE Local Cost Depolarizing-Noise Resilience]].

# References

[[2021 - Quantum autoencoders with enhanced data encoding.pdf]]
