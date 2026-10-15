2026-10-15 00:05

Status: #baby

Tags: [[Quantum and Hybrid Convolutional Image Classification]]

# Computational-Basis Phase Failure of Z-Angle Encoding

Encoding a feature with an $R_Z$ rotation fails when the target qubit begins in a computational-basis state and no preceding operation creates a phase-sensitive superposition. On $|0\rangle$ or $|1\rangle$, the rotation changes only a global phase, so the physical state and every later measurement probability remain independent of the feature.

This structural error appeared directly in the HQNN-Parallel sweep: the $R_Z$ angle encoding stayed at about 10% accuracy on a balanced ten-class problem, which is chance-level performance. The failure is not evidence that phase encodings are intrinsically useless. It shows that an encoding gate must be evaluated relative to its initial state and subsequent circuit; adding a basis-changing operation before the rotation could turn the phase into a relative, observable quantity.

# References

[[2025 - Practical insights on the effect of different encodings ansatze and measurements in quantum and hybrid convolutional neural networks.pdf]]
