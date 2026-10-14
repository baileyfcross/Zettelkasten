2026-10-12 02:08

Status: #baby

Tags: [[Quantum Convolutional Neural Networks]]

# QCNN Reverse MERA Interpretation

A quantum convolutional neural network has the circuit structure of a multiscale entanglement renormalization ansatz, or MERA, run in reverse. MERA builds a many-body state by repeatedly adding prepared qubits and applying isometries and local unitaries, whereas a QCNN progressively removes degrees of freedom from an existing state.

If a state has a MERA representation, the inverse MERA circuit provides a QCNN that recognizes that representative state with deterministic outcomes. Running the corresponding QCNN backward instead gives a hierarchical encoding or state-preparation circuit.

QCNNs add capabilities not present in a bare inverse MERA because their pooling measurements can act as error syndromes. This distinction links the representation of a phase's fixed-point state to the corrective behavior described by [[QCNN Nested Error Correction and Renormalization Flow]].

# References

[[2019 - Quantum Convolutional Neural Networks.pdf]]
