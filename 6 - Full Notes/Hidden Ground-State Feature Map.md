2026-10-14 09:01

Status: #baby

Tags: [[Quantum Convolutional Neural Networks]]

# Hidden Ground-State Feature Map

Quantum training data can conceal a feature map even when the learner receives states rather than explicit classical feature vectors. A physical preparation process maps underlying parameters such as field strengths, temperatures, or anisotropies to states $\rho(x)$, making that process an implicit or hidden embedding of $x$.

The paper studies ground-state preparation as this hidden map. Instead of choosing a rotation-based encoding first, it regards the parameterized Hamiltonian and the procedure that prepares its ground state as the source of the model's basis functions. The input state can therefore carry a strong problem-specific inductive bias before any trainable [[Quantum Convolutional Neural Network]] layer is applied.

For a Hamiltonian with a phase transition, the embedded state changes rapidly near its critical parameter. This gives the model basis functions that naturally support a sharp decision boundary, while the QCNN learns which combinations of those functions are useful. [[Ground-State Embedding Basis Functions]] make this mechanism explicit.

# References

[[2023 - What can we learn from quantum convolutional neural networks.pdf]]
