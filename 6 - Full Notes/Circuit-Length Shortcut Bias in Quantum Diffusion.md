2026-10-12 20:13

Status: #baby

Tags: [[Diffusion Models for Quantum Circuit Synthesis]]

# Circuit-Length Shortcut Bias in Quantum Diffusion

The entanglement generator learns a correlation between target entanglement and circuit length: requests with more entangled qubits produce length distributions whose peaks shift toward longer circuits. Those peaks coincide with lengths at which randomly generated circuits most often satisfy the requested property.

The paper interprets this as a shortcut for reducing denoising loss. Although the training data are balanced by circuit length within each condition, several balancing variants retain similar generated distributions. The bias helps explain why [[Quantum Circuit Diffusion Editing]] struggles when a long, highly entangled input must be continued into a low-entanglement target that the model associates with short circuits.

Generation is not completely locked to the preferred length. Changing the input tensor size constrains the maximum, and the model can still produce other feasible lengths. The result nevertheless shows that novelty and target accuracy do not prove that a generative circuit model learned the intended physical mechanism.

# References

[[2023 - Quantum circuit synthesis with diffusion models.pdf]]
