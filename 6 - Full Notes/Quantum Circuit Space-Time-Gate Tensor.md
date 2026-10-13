2026-10-12 20:13

Status: #baby

Tags: [[Diffusion Models for Quantum Circuit Synthesis]]

# Quantum Circuit Space-Time-Gate Tensor

A quantum circuit space-time-gate tensor represents the qubit index on one axis, the gate-placement time on a second, and a continuous gate embedding on a third. The encoding permits one gate at each time step and can vary in both qubit count and maximum circuit length.

Single-qubit gates use their assigned vectors directly. A multi-qubit gate places the same embedding on its control and target qubits with opposite signs, preserving the relationship between its endpoints even for nonlocal connections. The paper chooses mutually orthogonal embeddings, plus padding and background tokens, to make decoding robust to numerical variation.

Generated vectors are decoded by selecting the known gate embedding with greatest absolute cosine similarity and using the similarity sign to recover control versus target. Invalid outputs are those with conflicting gates at one time or incomplete multi-qubit endpoints. This representation supplies the input and output format for the [[Size-Generalizing Quantum Circuit Diffusion Architecture]].

# References

[[2023 - Quantum circuit synthesis with diffusion models.pdf]]
