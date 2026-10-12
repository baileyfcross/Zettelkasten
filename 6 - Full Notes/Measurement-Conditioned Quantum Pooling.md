2026-10-12 02:08

Status: #baby

Tags: [[Quantum Convolutional Neural Networks]]

# Measurement-Conditioned Quantum Pooling

Measurement-conditioned quantum pooling reduces the number of active qubits in a [[Quantum Convolutional Neural Network]]. A fraction of the register is measured, and each outcome determines a unitary correction applied to nearby qubits that remain in the circuit.

The reduction supplies the hierarchy and effective nonlinearity associated with pooling. Because the measurement results act like error syndromes, pooling can remove local perturbations while carrying coarse phase information into the next layer. Repeating the process lowers the system size until a final unitary can act on all surviving qubits.

Intermediate physical measurements are not essential to the logical construction. The paper notes that they can be postponed to the end by replacing feed-forward operations with controlled unitaries acting on measured and unmeasured qubits, which can simplify an implementation whose platform favors coherent control.

# References

[[2019 - Quantum Convolutional Neural Networks.pdf]]
