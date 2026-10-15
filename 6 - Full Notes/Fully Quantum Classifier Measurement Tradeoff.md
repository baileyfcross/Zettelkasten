2026-10-15 00:05

Status: #baby

Tags: [[Quantum and Hybrid Convolutional Image Classification]]

# Fully Quantum Classifier Measurement Tradeoff

Measurement choice had a much larger effect in the fully quantum classifiers than in the hybrid models. Computational-basis expectations performed best overall and used one measured qubit per class. Histogram readout assigned basis states to classes and predicted the class associated with the most frequent sampled outcome. Multiqubit Pauli strings offered many possible observables but produced wide accuracy dispersion because the selected operators were sampled from a very large space.

For four classes, the best shallow QCNN configuration reached 68.5% with flattened amplitude ordering and Pauli $Z$ readout. For ten classes, a multiqubit-Pauli configuration reached 42.5%, but operator choice remained a major uncontrolled variable. With no classical feature processor after the circuit, an observable must directly expose the class separation, so extra measurement complexity is useful only when the selected operator aligns with the learned state.

# References

[[2025 - Practical insights on the effect of different encodings ansatze and measurements in quantum and hybrid convolutional neural networks.pdf]]
