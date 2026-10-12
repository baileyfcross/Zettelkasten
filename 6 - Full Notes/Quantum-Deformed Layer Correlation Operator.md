2026-10-12 02:19

Status: #baby

Tags: [[Quantum-Deformed Probabilistic Neural Networks]]

# Quantum-Deformed Layer Correlation Operator

The correlation mechanism of a quantum-deformed layer is a unitary operator that changes the joint basis of activation and weight qubits before their binary preactivations are measured. If the undeformed input state assigns amplitudes to activation-weight bit strings, the squared amplitudes after applying the unitary define a new joint probability distribution over those strings.

A nontrivial unitary can entangle activation and weight registers, so the new distribution need not factor into independent terms. Identity deformation restores the original probabilistic binary layer, while more expressive circuits can introduce nonlocal correlations that are expensive to sample classically.

The same operator is trainable alongside the probabilistic weight parameters. Its expressive benefit and its computational cost depend strongly on circuit structure: general entangling choices motivate [[Quantum-Deformed Sampling Speedup]], whereas the paper's experiments restrict the operator to the neighboring gates used by [[Low-Entanglement Classical QDNN Simulation]].

# References

[[2020 - Quantum Deformed Neural Networks.pdf]]
