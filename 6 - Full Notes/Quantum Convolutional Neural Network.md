2026-10-12 02:08

Status: #baby

Tags: [[Quantum Convolutional Neural Networks]]

# Quantum Convolutional Neural Network

A quantum convolutional neural network, or QCNN, is a hierarchical quantum circuit for classifying an unknown many-qubit state or learning a quantum error-correcting code. Its repeated stages apply shared local unitaries, reduce the active system through measurement-conditioned pooling, and end with a unitary on the remaining qubits followed by a fixed number of measurements.

The architecture adapts the locality, [[Convolutional Weight Sharing]], and progressive size reduction of a classical [[Convolutional Neural Network]] without treating quantum amplitudes as an ordinary image. Its trainable objects are quantum unitaries, and its pooling outcomes can control correction operations on qubits that remain active.

The paper interprets this circuit as both a reversed entanglement-renormalization network and a nested error-correction process. Those two views explain its applications to [[QCNN Symmetry-Protected Phase Recognition]] and [[QCNN-Optimized Quantum Error Correction]].

A later analysis also treats the circuit as a measurement adapter. Conjugating its final few-qubit observable through the QCNN produces an effective many-body observable, so pooling can select basis functions supplied by a [[Hidden Ground-State Feature Map]]. This view extends the architecture from phase classification to finite-shot learning and regression.

# References

[[2019 - Quantum Convolutional Neural Networks.pdf]]

[[2023 - What can we learn from quantum convolutional neural networks.pdf]]
