2026-10-12 20:13

Status: #baby

Tags: [[Diffusion Models for Quantum Circuit Synthesis]]

# Quantum Circuit Diffusion Dataset Curation

The circuit-diffusion datasets are built by sampling random gate subsets, gate counts, and placements, then calculating the condition associated with each circuit. Entanglement examples receive text descriptions of their Schmidt-rank vectors, while compilation examples pair a target unitary with a prompt naming the gate set used to create it.

Before training, Qiskit's circuit optimizer removes redundant consecutive gates and improves the examples, after which duplicate circuits are deleted. The remaining data are balanced first across conditions and then across circuit lengths within each condition. The authors report that both optimization and balancing materially improve model accuracy.

The entanglement dataset covers three through eight qubits with H and CX gates. The compilation dataset contains 2.5 million distinct three-qubit circuits derived from 1.17 million distinct unitaries and uses circuits of two through twelve gates. These large labeled corpora explain why [[Few-Sample Quantum Circuit Diffusion Adaptation]] is useful while also motivating [[Quantum Circuit Diffusion Scalability Limits]].

# References

[[2023 - Quantum circuit synthesis with diffusion models.pdf]]
