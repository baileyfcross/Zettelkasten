2026-10-15 00:05

Status: #baby

Tags: [[Quantum and Hybrid Convolutional Image Classification]]

# Encoding Dominance in Hybrid Quantum Classifiers

In the paper's two hybrid image classifiers, the data-to-state encoding changed validation accuracy far more than the variational ansatz or single-qubit measurement basis. Across encodings, performance varied by more than 30 percentage points; changing ansatzes or choosing among Pauli $X$, $Y$, and $Z$ measurements generally moved accuracy by less than five points.

The ranking was architecture-dependent rather than universal. IQP, angle, and some QAOA encodings worked well after classical feature extraction in HQNN-Parallel. For the early quanvolution, angle, ring, and waterfall encodings were useful, IQP was intermediate, and amplitude and QAOA encodings performed poorly. Encoding therefore should be selected together with where the circuit sits and what representation it receives, instead of being treated as a preprocessing choice independent of network structure.

# References

[[2025 - Practical insights on the effect of different encodings ansatze and measurements in quantum and hybrid convolutional neural networks.pdf]]
