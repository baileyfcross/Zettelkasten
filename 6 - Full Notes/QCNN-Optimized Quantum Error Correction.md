2026-10-12 02:08

Status: #baby

Tags: [[Quantum Convolutional Neural Networks]]

# QCNN-Optimized Quantum Error Correction

A QCNN and its inverse define decoding and encoding channels that can be optimized together for a particular quantum noise process. The training objective averages recovery fidelity over the six Pauli-axis eigenstates of one logical qubit, and it can be evaluated experimentally even when the physical error channel is not known analytically.

The paper simulates a two-layer circuit that encodes one logical qubit into nine physical qubits. For independent isotropic single-qubit errors, training matches known codes of comparable structure. For anisotropic errors it can lower the logical error rate by a model-dependent constant factor, and for the studied correlated-error model it substantially outperforms the nine-qubit Shor code.

Optimization is performed layer by layer because simultaneous gradient descent becomes trapped in a local optimum. The first layer is trained to concentrate its effective channel into one dominant error type, and the second layer corrects the remaining simpler channel. These results are numerical and tailored to specified error models rather than a universal replacement for established codes.

# References

[[2019 - Quantum Convolutional Neural Networks.pdf]]
