2026-10-12 20:13

Status: #baby

Tags: [[Diffusion Models for Quantum Circuit Synthesis]]

# Quantum Circuit Diffusion Editing

Quantum circuit diffusion editing fixes an existing gate prefix in the circuit tensor and denoises only a designated continuation region. This lets the generator accept a prepared input state and synthesize additional gates intended to transform its entanglement pattern toward a requested target.

The paper edits five-qubit circuits with at most twenty gates, reserving at most the first six gates for the input circuit. It samples 1,024 continuations for each of 256 initial circuits and checks whether at least one realizes the target Schmidt-rank vector. Increasing entanglement is generally easier than removing it.

The hardest cases begin fully entangled and request substantial disentanglement, which generally needs a longer continuation while the model associates low entanglement with shorter circuits. Even in the reported worst aggregate case, at least one correct edit is found for 89.1 percent of initial circuits. Editing reuses a trained model but still depends on repeated sampling and verification.

# References

[[2023 - Quantum circuit synthesis with diffusion models.pdf]]
