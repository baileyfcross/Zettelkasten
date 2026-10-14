2026-10-12 20:13

Status: #baby

Tags: [[Diffusion Models for Quantum Circuit Synthesis]]

# Size-Generalizing Quantum Circuit Diffusion Architecture

The paper adapts a residual U-Net so one model can accept circuit tensors with different qubit counts and time lengths. Convolutions operate only along the time axis, avoiding a local receptive-field assumption across qubits, while self-attention spans the complete qubit dimension so distant control-target relationships remain visible.

Two-dimensional sinusoidal position encoding identifies absolute qubit and time locations. Circuit lengths are padded to multiples of four for downsampling and upsampling. Training first pads every example to a global maximum, then fine-tunes with buckets of equal qubit count and trims each batch to its longest time dimension; the bucket stage substantially improves reported accuracy.

At inference, the noisy input tensor determines the output qubit count and maximum gate count. A learned padding token lets the model return a shorter circuit than the tensor permits. This flexibility underlies both [[Topology-Constrained Circuit Diffusion Masking]] and the nearly stable entanglement accuracy observed across sufficiently large tensor lengths.

# References

[[2023 - Quantum circuit synthesis with diffusion models.pdf]]
