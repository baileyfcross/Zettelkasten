2026-10-12 20:13

Status: #baby

Tags: [[Diffusion Models for Quantum Circuit Synthesis]]

# Diffusion-Generated Entanglement Circuits

The paper conditions circuit generation on a Schmidt-rank vector whose entry for each qubit is one when that qubit is unentangled and two when it is entangled with the remainder. Training examples use H and CX circuits with three through eight qubits and circuit lengths ranging from two to fifty-two gates before optimization.

After training, 99.6 percent of generated continuous tensors decode into structurally valid circuits. Most generated circuits produce the requested entanglement pattern, although accuracy declines as the number of entangled qubits grows because those targets generally require more gates. Sampling several inexpensive candidates and verifying only the small candidate set can recover usable solutions when one draw fails.

Generated circuits are overwhelmingly absent from the training set and distinct within a generated batch, showing that the model is not limited to retrieving memorized sequences. This novelty result is paired with a caveat: [[Circuit-Length Shortcut Bias in Quantum Diffusion]] shows that the model also learns a length-entanglement correlation from the task.

# References

[[2023 - Quantum circuit synthesis with diffusion models.pdf]]
