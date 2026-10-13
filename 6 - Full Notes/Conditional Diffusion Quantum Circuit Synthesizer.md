2026-10-12 20:13

Status: #baby

Tags: [[Diffusion Models for Quantum Circuit Synthesis]]

# Conditional Diffusion Quantum Circuit Synthesizer

A conditional diffusion quantum circuit synthesizer begins with a noisy circuit-shaped tensor and iteratively denoises it into a discrete gate sequence guided by a requested property. The request can describe an entanglement pattern, an allowed gate set, or a target unitary represented by a learned encoder.

Training uses corrupted examples of valid circuits rather than scoring every generated circuit against a quantum target. This shifts the learned task from directly optimizing quantum behavior to modeling the distribution of circuits associated with each condition. [[Denoising-Loss Quantum Circuit Synthesis]] explains why this avoids circuit simulation inside the training loss without eliminating the cost of constructing the dataset.

The paper demonstrates generation of H-and-CX circuits with specified entanglement and compilation of three-qubit unitaries into restricted gate sets. It also supports [[Topology-Constrained Circuit Diffusion Masking]] and [[Quantum Circuit Diffusion Editing]] without retraining. These results are classical simulations of small circuits, not a hardware demonstration or a general scalability guarantee.

# References

[[2023 - Quantum circuit synthesis with diffusion models.pdf]]
