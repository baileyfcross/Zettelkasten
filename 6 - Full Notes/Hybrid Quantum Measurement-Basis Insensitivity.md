2026-10-15 00:05

Status: #baby

Tags: [[Quantum and Hybrid Convolutional Image Classification]]

# Hybrid Quantum Measurement-Basis Insensitivity

Measuring local qubits in the Pauli $X$, $Y$, or $Z$ basis produced similar validation-accuracy distributions in both hybrid architectures. A small tendency favored the computational basis in HQNN-Parallel, but the total effect was minor compared with changing the encoding.

The three measurements are closely related by single-qubit rotations, and later classical layers can learn to combine whichever Bloch-vector projection they receive. That downstream flexibility can make local basis choice less decisive than it would be in a fully quantum classifier. The finding is limited to local single-qubit observables in noiseless simulations; multiqubit measurements or hardware-dependent readout errors could produce a different ranking. It should not be generalized into a claim that measurement design is irrelevant to hybrid quantum learning.

# References

[[2025 - Practical insights on the effect of different encodings ansatze and measurements in quantum and hybrid convolutional neural networks.pdf]]
