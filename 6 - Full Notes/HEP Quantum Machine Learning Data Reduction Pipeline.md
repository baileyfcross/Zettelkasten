2026-10-15 00:14

Status: #baby

Tags: [[Quantum Computing for High-Energy Physics]]

# HEP Quantum Machine Learning Data Reduction Pipeline

Experimental high-energy-physics datasets combine very large event counts with tens or hundreds of features per event. Present quantum processors cannot accept that scale directly, so most proposed workflows first use classical feature extraction, dimensionality reduction, or an autoencoder to create a compact latent representation and then embed that representation into a quantum state.

Trainable compression can be optimized jointly with the quantum model. In a signal-versus-background classifier, end-to-end training encourages the latent coordinates to preserve class separation rather than merely reconstruct the input. The quantum stage then acts on fewer variables, but its apparent performance includes the inductive bias and information loss introduced by the classical front end.

State preparation creates another tradeoff. A compact amplitude encoding can use qubits efficiently while requiring a costly circuit for arbitrary data; simpler angle encodings may use more qubits but map more directly to shallow operations. A credible comparison must include compression, loading, training, measurements, and generalization rather than evaluating only the central circuit. This pipeline underlies [[Quantum Rare-Signal Extraction in HEP]] and [[Quantum Generative Detector Simulation]].

# References

[[2023 - Quantum Computing for High-Energy Physics State of the Art and Challenges Summary of the QC4HEP Working Group.pdf]]
