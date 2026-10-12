2026-10-12 18:44

Status: #baby

Tags: [[Quantum Dropout Regularization]]

# Canonical Quantum Dropout

Canonical quantum dropout removes a selected one-qubit rotation together with entangling gates connected to its qubit: preceding entanglers for which that qubit is the target and subsequent entanglers for which it is the control. This structured group is intended to approximate the classical act of dropping a neuron and its incident connections without making the quantum state change as drastic as deleting every gate touching the qubit.

Canonical-forward dropout is a partial variant. It removes the rotation and only the subsequent entanglers that use the same qubit as control; a backward-only version is conceptually analogous, so the paper evaluates the forward form. In the classification circuit, canonical and canonical-forward coincide because each data-reuploading layer contains only one variational sublayer.

The analogy to a dropped classical neuron remains incomplete. Entanglement lets a rotation affect other qubits, and reuse of a qubit across circuit depth preserves a temporal connection that this operation group does not remove. Canonical dropout is therefore a quantum-specific compromise rather than a literal translation of neural-network connectivity.

# References

[[2023 - A General Approach to Dropout in Quantum Neural Networks.pdf]]
