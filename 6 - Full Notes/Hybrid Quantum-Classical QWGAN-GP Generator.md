2026-10-16 17:54

Status: #baby

Tags: [[Variational Quantum Wasserstein Anomaly Detection]]

# Hybrid Quantum-Classical QWGAN-GP Generator

The QWGAN-GP generator is a composition of a quantum feature map and a classical upscaling layer. An $N$-qubit parameterized circuit converts $N$ latent variables into $N$ Pauli-$Z$ expectations, and a dense sigmoid layer maps those expectations into the $M$-dimensional data space. For the full credit-card benchmark, $M=29$ while $N$ can be smaller.

The classical critic is unchanged from the WGAN-GP baseline. This controlled substitution attributes differences between the two models to the generator's first block rather than to different critics, losses, or output layers. It also means the quantum device never receives a 29-dimensional transaction record: [[Quantum Latent Rotation Encoding]] loads only the low-dimensional random input.

The architecture trades a classical-data loading problem for repeated quantum expectation estimation. It may be useful if a circuit samples a latent distribution that is difficult to reproduce classically, but the benchmark does not demonstrate such a sampling advantage. [[Commuting Z-Expectation Generator Readout]] explains how the circuit output is exposed to the classical network.

# References

[[2021 - Anomaly detection with variational quantum generative adversarial networks.pdf]]
