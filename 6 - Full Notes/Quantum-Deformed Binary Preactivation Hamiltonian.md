2026-10-12 02:19

Status: #baby

Tags: [[Quantum-Deformed Probabilistic Neural Networks]]

# Quantum-Deformed Binary Preactivation Hamiltonian

The binary preactivation Hamiltonian is a sum of pairwise products between each input-activation bit operator and its corresponding weight-bit operator. On a computational-basis state, its eigenvalue is the number of positions at which both bits equal one, exactly matching the binary layer's integer preactivation.

Because the Hamiltonian is diagonal and decomposes into commuting two-qubit terms, its time-evolution operator can be assembled efficiently from diagonal two-qubit quantum gates. The paper uses that controlled evolution inside [[QPE Threshold Activation]] so the network can extract a neuron output without classically sampling every activation and weight.

A deformation unitary conjugates this Hamiltonian evolution. That preserves its eigenvalues but rotates its eigenvectors, turning the same preactivation spectrum into the correlated measurement law of the [[Quantum-Deformed Layer Correlation Operator]].

# References

[[2020 - Quantum Deformed Neural Networks.pdf]]
