2026-10-12 20:13

Status: #baby

Tags: [[Diffusion Models for Quantum Circuit Synthesis]]

# Quantum Circuit Diffusion Scalability Limits

The denoising network can in principle be enlarged and its tensor axes extended to many qubits and gates, but model capacity is not the paper's main scalability barrier. Training data still require classically calculating the property attached to each source circuit, such as its output entanglement or full unitary.

Unitary compilation has an additional exponential bottleneck because the conditioning matrix itself grows as the square of the Hilbert-space dimension. A larger U-Net does not change that representation cost. The authors suggest that a more compact condition, such as a Hamiltonian generating the desired evolution, may be necessary for large systems.

[[Few-Sample Quantum Circuit Diffusion Adaptation]] reduces the number of new examples needed when moving from eight to nine or ten qubits and may be practical for systems with tens of qubits. The paper does not show that it remains sufficient for hundreds or thousands, nor does it eliminate the need to verify sampled circuits. Scalability claims must therefore separate neural-network size from quantum-label and conditioning costs.

# References

[[2023 - Quantum circuit synthesis with diffusion models.pdf]]
