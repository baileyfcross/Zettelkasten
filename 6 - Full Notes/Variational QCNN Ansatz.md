2026-10-14 09:01

Status: #baby

Tags: [[Quantum Convolutional Neural Networks]]

# Variational QCNN Ansatz

The paper turns its fixed cluster-state QCNN into a trainable ansatz by replacing basis changes with arbitrary single-qubit rotations and replacing fixed pivoting interactions with adjustable $ZZ$ rotations. Translational invariance shares the same parameters across equivalent locations in a convolution layer.

Its pooling layers use controlled trainable rotations rather than mandatory mid-circuit measurements. This coherent form follows the deferred-measurement principle used by [[Measurement-Conditioned Quantum Pooling]] while retaining the 9-to-3-to-1 hierarchy.

Using only four labeled training points, the guided ansatz learns a sharp phase boundary and reaches perfect accuracy on the paper's 100-point test set. A more arbitrary ansatz built from neighboring two-qubit unitaries also reaches perfect test accuracy, although with a less saturated boundary away from criticality. The comparison indicates that much of the task's favorable structure comes from the [[Hidden Ground-State Feature Map]], while the variational circuit adapts how that structure is read out.

# References

[[2023 - What can we learn from quantum convolutional neural networks.pdf]]
