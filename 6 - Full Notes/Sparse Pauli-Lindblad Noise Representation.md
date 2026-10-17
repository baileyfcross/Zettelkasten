2026-10-17 11:34

Status: #baby

Tags: [[Scalable Error-Mitigated Quantum Simulation]]

# Sparse Pauli-Lindblad Noise Representation

Pauli twirling can convert local hardware noise into a sparse Pauli-Lindblad model whose generators are one-qubit Pauli operators and correlated two-qubit Pauli products on neighboring qubits. With nearest-neighbor crosstalk, the number of relaxation rates grows linearly with the number of qubits, and the model can be represented as a diagonal matrix-product operator with bond dimension four.

Every Pauli string is an eigenoperator of this noise. Its fidelity is the product of exponential damping factors associated with exactly those generators that anticommute with it. Because a nontrivial Pauli string anticommutes with half of all Pauli strings, typical high-weight observables cluster around a geometric-mean damping factor that connects the learned rates to [[Error Density in Layered Quantum Circuits]].

# References

[[2024 - Scalability of quantum error mitigation techniques from utility to advantage.pdf]]

