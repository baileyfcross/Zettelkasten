2026-10-14 09:01

Status: #baby

Tags: [[Quantum Convolutional Neural Networks]]

# QCNN Error-Correction Criterion

The error-correction criterion requires QCNN pooling to remove symmetry-compatible local deviations from a phase's representative state. In the cluster model, moving away from the fixed point introduces effective bit-flip patterns after the pivoting and basis-change layers.

The fixed circuit detects those patterns on qubits that will be discarded and uses controlled operations, including Toffoli gates, to correct the qubits that survive pooling. Deferred measurement allows the correction to be implemented coherently before the discarded qubits are traced out. The construction protects the pooled output from the lowest-order errors analyzed in the paper.

Together with the [[QCNN Fixed-Point Criterion]], this turns coarse graining into a denoising process: the ideal state is reproduced at smaller scale, while nearby states are pushed back toward it. This is the circuit-level mechanism behind [[QCNN Nested Error Correction and Renormalization Flow]].

# References

[[2023 - What can we learn from quantum convolutional neural networks.pdf]]
