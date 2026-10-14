2026-10-14 09:01

Status: #baby

Tags: [[Quantum Convolutional Neural Networks]]

# Ground-State Embedding Basis Functions

If a parameterized ground state is expanded as $|\psi_0(x)\rangle=\sum_j\phi_j(x)|j\rangle$, its amplitudes and their products act as feature-dependent basis functions for a quantum model. An observable determines which diagonal probabilities or off-diagonal products are combined into the final expectation value.

In the paper's three-qubit cluster-model example, the computational-basis probabilities change abruptly near the critical point. The string-order observable selects antidiagonal amplitude products, and their sum forms a sigmoid-like expectation that separates the symmetry-protected and trivial phases even before a trainable circuit is introduced.

This means the sharp boundary is primarily supplied by the [[Hidden Ground-State Feature Map]], not manufactured from scratch by variational parameters. A QCNN then transforms the measurement so it can emphasize the useful members of this basis, as described by [[QCNN Measurement Adaptation]].

# References

[[2023 - What can we learn from quantum convolutional neural networks.pdf]]
