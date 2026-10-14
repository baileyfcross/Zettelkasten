2026-10-12 01:33

Status: #baby

Tags: [[Enhanced Feature Quantum Autoencoders]]

# Entanglement-Focused QAE Ansatz

An entanglement-focused quantum-autoencoder ansatz concentrates its two-qubit gates where disentangling is required for compression. The circuit emphasizes interactions among trash qubits and between trash and latent qubits, while avoiding unnecessary entanglers solely among qubits that remain in the compressed state.

The paper's construction alternates parameterized single-qubit Y rotations with controlled-Z gates. Many entangling gates can be applied in parallel, and the gate count grows linearly with the number of qubits and repeated layers. A final rotation layer acts on the trash qubits before measurement.

This design reflects the operational goal of moving information out of [[Quantum Autoencoder Trash Space]] while keeping the circuit shallow enough for limited-coherence devices. In the enhanced model, the single-qubit rotations implement [[Linear Feature Reuploading in EF-QAE]], so the same entanglement pattern supports feature-dependent compression.

# References

[[2021 - Quantum autoencoders with enhanced data encoding.pdf]]
