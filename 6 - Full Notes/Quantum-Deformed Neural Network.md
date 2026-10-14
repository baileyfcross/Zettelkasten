2026-10-12 02:19

Status: #baby

Tags: [[Quantum-Deformed Probabilistic Neural Networks]]

# Quantum-Deformed Neural Network

A quantum-deformed neural network is a probabilistic binary neural network whose usual independent activation and weight distributions are transformed by an entangling quantum circuit before each layer computes its outputs. The resulting correlations enlarge the layer's distribution family while retaining ordinary binary data at the input and ordinary class probabilities at the output.

The construction encodes activation and weight bits as qubits, uses [[Quantum-Deformed Binary Preactivation Hamiltonian]] eigenvalues to represent weighted sums, and applies [[QPE Threshold Activation]] to obtain binary neuron outputs. A deformation unitary changes the basis in which those preactivations are evaluated, producing the correlated distribution described by the [[Quantum-Deformed Layer Correlation Operator]].

The full proposal targets error-corrected quantum hardware because it depends on quantum phase estimation. The paper's experiments instead use a restricted low-entanglement deformation that admits [[Low-Entanglement Classical QDNN Simulation]], so their measured accuracy gains do not demonstrate a quantum-computational or learning advantage.

# References

[[2020 - Quantum Deformed Neural Networks.pdf]]
