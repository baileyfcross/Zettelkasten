2026-10-14 09:01

Status: #baby

Tags: [[Quantum Convolutional Neural Networks]]

# QCNN Fixed-Point Criterion

The fixed-point criterion requires a QCNN layer to map a representative state of the target phase to a smaller copy of the same representative state. For the paper's cluster state, pivoting and Hadamard gates first unprepare the state to computational zeros, so the qubits selected for removal have deterministic outcomes.

After pooling retains one qubit out of each three, inverse basis changes reprepare the cluster state on the surviving register. The resulting 9-to-3-to-1 flow preserves the phase representative while successively reducing the number of active qubits.

This criterion explains why the target state is stable under coarse graining and connects the circuit to [[QCNN Reverse MERA Interpretation]]. It is paired with the [[QCNN Error-Correction Criterion]], which determines how nearby perturbed states are driven toward the same fixed point rather than merely preserving the ideal state.

# References

[[2023 - What can we learn from quantum convolutional neural networks.pdf]]
